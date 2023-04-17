import os
import pathlib
import pandas as pd
import xlwings as xw
import openpyxl
import requests # request img from web
import shutil # save img locally
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from openpyxl import load_workbook
from openpyxl.drawing.spreadsheet_drawing import AbsoluteAnchor
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from forms.models import Form, Responses, Answer, Choices
from accounts.models import Profile
from django.contrib.auth.models import User

def select_data(code):
  responses = Responses.objects.get(response_code=code)
  form = responses.response_to
  df_questions = pd.DataFrame(columns=['order','name_label','question','yes','no'])
  df_obs = pd.DataFrame(columns=['item','description'])
  answers = responses.response.all()
  for answer in answers:
    question = answer.answer_to.question
    label = '-'
    order = '-'
    if answer.answer_to.label:
      label = answer.answer_to.label.name
      order = str(answer.answer_to.label.order)
    if answer.answer_to.question_type == 'multiple choice':
      id_choice = answer.answer
      obj_choice = Choices.objects.get(id=id_choice)
      bool_positive = ''
      bool_negative = ''
      if 'No' in obj_choice.choice:
        bool_negative = 'X'
      else:
        bool_positive = 'X'
      row = [order, label, question, bool_positive, bool_negative]
      df_questions.loc[len(df_questions)] = row
    elif answer.answer_to.question_type == 'short':
      answer_obs = answer.answer
      row = ['1',answer_obs]
      df_obs.loc[len(df_obs)] = row
  #Clever Apaza
  user_supervisor = User.objects.get(username=24339)
  data_supervisor = get_data(user_supervisor)
  data_tech = get_data(responses.responder)
  return {
    'questions': df_questions,
    'obs': df_obs,
    'supervisor_user': data_supervisor,
    'tech_user': data_tech
  }

def get_data(user):
  profile = Profile.objects.get(user=user)
  url_signature = None
  if profile.signature:
    url_signature = f"https://res.cloudinary.com/johguxo-gonzales/{profile.signature}"
  data = [user.get_full_name(), profile.code]
  data_frame = pd.DataFrame(data, columns=["data"])
  return {
    'data': data_frame,
    'name': user.get_full_name(),
    'signature': url_signature
  }


def download_images(url_images):
  images = []
  index = 0
  for url_image in url_images:
    if index == 0:
      filename = 'forms/static/files/firma_tecnico.png'
    else:
      filename = 'forms/static/files/firma_supervisor.png'
    res = requests.get(url_image, stream = True)
    if res.status_code == 200:
      with open(filename, 'wb') as f:
        shutil.copyfileobj(res.raw, f)
    index += 1
  return images

def excel_responses(code):
  data = select_data(code)
  data_questions = data['questions']
  data_obs = data['obs']
  data_tech = data['tech_user']['data']
  data_supervisor = data['supervisor_user']['data']
  signatures = download_images([data['tech_user']['signature'],
                               data['supervisor_user']['signature']])
  #absolute_path = os.path.abspath("./static/files/master_template.xlsx")
  #path_file = pathlib.Path(absolute_path).as_uri()
  #master_wb = xw.Book(absolute_path)
  writer = pd.ExcelWriter("forms/static/files/master_template.xlsx",
                          mode="a",
                          engine='openpyxl',
                          if_sheet_exists="overlay")
  data_questions.to_excel(writer,
                          sheet_name='Sheet1',
                          startrow=8,
                          startcol=0,
                          header=False,
                          index=False)
  data_obs.to_excel(writer,
                    sheet_name='Sheet1',
                    startrow=40,
                    startcol=1,
                    header=False,
                    index=False)
  workbook = writer.book
  worksheet = workbook.worksheets[0]
  #Insert data technical user
  image = openpyxl.drawing.image.Image(str('forms/static/files/firma_tecnico.png'))
  worksheet.add_image(image,'C53')
  data_tech.to_excel(writer,
                    sheet_name='Sheet1',
                    startrow=53,
                    startcol=2,
                    header=False,
                    index=False)
  #Insert data supervisor user
  image = openpyxl.drawing.image.Image(str('forms/static/files/firma_supervisor.png'))
  worksheet.add_image(image,'C48')
  data_supervisor.to_excel(writer,
                    sheet_name='Sheet1',
                    startrow=48,
                    startcol=2,
                    header=False,
                    index=False)
  writer.close()
  send_file(data['tech_user']['name'])
  clear_file()

def clear_file():
  #New file with original replace master_template
  os.remove('forms/static/files/master_template.xlsx')
  shutil.copy('forms/static/files/master_template_original.xlsx',
              'forms/static/files/master_template_copy.xlsx')
  os.rename('forms/static/files/master_template_copy.xlsx',
            'forms/static/files/master_template.xlsx')

def send_file(user_full_name):
  #email = 'tmm@ferreyros.com.pe'
  send_from = 'tmmpruebas123@gmail.com'
  send_to = ['carlosrosel105@gmail.com','tmm@ferreyros.com.pe','jgonzalesi@uni.pe']
  subject = 'Checklist - Metalizado de ' + user_full_name
  text = 'Se adjunta archivo de respuestas del Checklist de Metalizado de hoy por ' + user_full_name
  file = 'forms/static/files/master_template.xlsx'
  send_mail(send_from, send_to, subject, text, files=[file])


def send_mail(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    #Conection SMTP
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    correo = 'tmmpruebas123@gmail.com'
    pas = 'ovpoqmusorxdzyne'

    smtp.starttls()
    smtp.login(correo, pas)

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()