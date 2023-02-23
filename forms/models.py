from django.db import models
from django.utils import timezone
from machines.models import Machine

from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    status = models.BooleanField(default=True)
    date = models.DateField(null=True,blank=True,default=timezone.now)

    def __str__(self):
        return self.title

class QuestionDetail(models.Model):
    choices_type = (
        (0, 'TEXT'),
        (1, 'CHECKBOX'),
        (3, 'MULTISELECT'),
        (4, 'RADIO')
    )
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    type = models.IntegerField(choices=choices_type,default=0)


class Form(models.Model):
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)

    def __str__(self):
        return self.machine.title + '-'

class SectionForm(models.Model):
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    header = models.CharField(max_length=200,default='')

class UserForm(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True,default=timezone.now)

class AnswerUserForm(models.Model):
    user_form = models.ForeignKey(UserForm,on_delete=models.CASCADE)

