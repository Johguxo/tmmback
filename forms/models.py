from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.




class Choices(models.Model):
    choice = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.choice
    
    class Meta:
        ordering=['creation_date']

class Label(models.Model):
    name = models.CharField(max_length=200,default='')
    order = models.IntegerField(default=0)

    def __str__(self):
        return '[' + str(self.order) + '] '+ self.name

class Questions(models.Model):
    question = models.CharField(max_length=10000)
    question_type = models.CharField(max_length=20)
    label = models.ForeignKey(Label,on_delete=models.CASCADE,blank=True,null=True)
    required = models.BooleanField(default= False)
    answer_key = models.CharField(max_length = 5000, blank = True)
    score = models.IntegerField(blank = True, default=0)
    feedback = models.CharField(max_length = 5000, null = True, blank = True)
    choices = models.ManyToManyField(Choices, related_name = "choices")
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        str_label = 'No tiene etiqueta'
        if self.label:
            str_label = self.label.name
        return '(' + str_label + ') ' + self.question + ': ' + self.question_type

    class Meta:
        ordering=['creation_date']

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Questions, on_delete = models.CASCADE ,related_name = "answer_to")

class Form(models.Model):
    code = models.CharField(max_length=30,default='')
    title = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator", null=True)
    background_color = models.CharField(max_length=20, default = "#d9efed")
    text_color = models.CharField(max_length=20, default="#272124")
    collect_email = models.BooleanField(default=False)
    authenticated_responder = models.BooleanField(default = False)
    edit_after_submit = models.BooleanField(default=False)
    confirmation_message = models.CharField(max_length = 10000, default = "Your response has been recorded.")
    is_quiz = models.BooleanField(default=False)
    allow_view_score = models.BooleanField(default= True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    questions = models.ManyToManyField(Questions, related_name = "questions")

    def __str__(self):
        return self.title

class Responses(models.Model):
    response_code = models.CharField(max_length=20)
    response_to = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "response_to")
    responder_ip = models.CharField(max_length=30)
    responder = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "responder", blank = True, null = True)
    responder_email = models.EmailField(blank = True)
    response = models.ManyToManyField(Answer, related_name = "response")
    createdAt = models.DateTimeField(default=timezone.now)