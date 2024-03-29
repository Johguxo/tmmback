from django.db import models

from django.contrib.auth.models import User
from forms.models import Form
from cloudinary.models import CloudinaryField
# Create your models here.

class Machine(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    image = CloudinaryField('image')
    epp = CloudinaryField('epp', blank=True, null=True)
    form = models.ForeignKey(Form,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class UserMachine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() + '[ '+self.machine.title + ' ]'

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
    title = models.CharField(max_length=300, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(default='', blank=True)
    image = CloudinaryField('image')
    video_link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        if self.section:
            return '[' + self.section.machine.title + '] Section: ' + (self.section.name) + ' - ' + self.title
        elif self.subsection:
            return '[' + self.subsection.section.machine.title + '] Subsection: ' + (self.subsection.name) + ' - ' + self.title
        else:
            return 'No esta asociado'

class Incidents(models.Model):
    title = models.CharField(max_length=300, blank=True, default='')
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(default='')
    image = CloudinaryField('image')
    video_link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title