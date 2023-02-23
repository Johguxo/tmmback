from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  choices_roles = (
    (0, 'Trabajador'),
    (2, 'Ingeniero'),
    (1, 'Admin')
  )

  user = models.ForeignKey(User,on_delete=models.CASCADE)
  role = models.IntegerField(default=0,choices=choices_roles)
  
  def __str__(self):
    return self.user.get_full_name()

