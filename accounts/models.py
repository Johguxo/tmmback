from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.utils import timezone
import datetime
# Create your models here.

class Profile(models.Model):
  choices_roles = [
    (0, 'Trabajador'),
    (1, 'Ingeniero'),
    (2, 'Admin'),
  ]

  choices_levels = [
    (0, 'Machine Shop 1'),
    (1, 'Machine Shop 2'),
    (2, 'Machine Shop 3'),
    (3, 'Machine Shop 4'),
  ]

  choices_specialists = [
    (0, 'Metalizador'),
    (1, 'Fresador'),
    (2, 'Tornero'),
    (3, 'Supervisor'),
    (4, 'Administrativo'),
    (5, 'Jefatura'),
  ]

  user = models.ForeignKey(User,on_delete=models.CASCADE)
  image = CloudinaryField('image',blank=True, null=True)
  signature = CloudinaryField('signature',blank=True, null=True)
  role = models.IntegerField(default=0,choices=choices_roles)
  date_of_birth = models.DateField(default=timezone.now)
  code = models.CharField(max_length=50,null=True,blank=True)
  level = models.IntegerField(default=0,choices=choices_levels)
  date_of_admission = models.DateField(default=timezone.now)
  specialist = models.IntegerField(default=0,choices=choices_specialists)
  objectives = models.TextField(default='')

  
  def __str__(self):
    return self.user.get_full_name()
  
  def age(self):
    calculate_age = datetime.date.today().year - self.date_of_birth.year
    return calculate_age


class Skill(models.Model):
  name = models.CharField(max_length=100,default='')
  description = models.TextField(null=True,blank=True)

  def __str__(self):
    return self.name
  
class UserSkill(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  skill = models.ForeignKey(Skill,on_delete=models.CASCADE)

  def __str__(self):
    return self.user.get_full_name() + ' - ' + self.skill.name

class Achievement(models.Model):
  name = models.CharField(max_length=100,default='')

  def __str__(self):
    return self.name
  
class UserAchievement(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.get_full_name() + ' - ' + self.achievement.name