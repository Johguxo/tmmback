from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Machine(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

class UserMachine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()

class Section(models.Model):
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='')
    have_subsection = models.BooleanField(default=True)

    def __str__(self):
        bool_have_subsection = '1'
        if self.have_subsection:
            bool_have_subsection = '0'
        return (self.machine.title + ': ' + 
                self.name + '['+bool_have_subsection+']')

class SubSection(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='')

    def __str__(self):
        return (
            self.section.machine.title + ': '+
            self.section.name + ' - ' + self.name
        )

class Info(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE,blank=True,null=True)
    subsection  = models.ForeignKey(SubSection,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField(default='')
    image = CloudinaryField('image')
    video_link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        if self.section:
            return (self.section.name)
        elif self.subsection:
            return (self.subsection.name)
        else:
            return 'No esta asociado'

class IncidentsMachine(models.Model):
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)
    content = models.TextField(default='')
    image = CloudinaryField('image')
    video_link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.machine.title