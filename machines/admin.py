from django.contrib import admin
from machines.models import (Machine, UserMachine, 
      Info, Section,SubSection,IncidentsMachine)
# Register your models here.

admin.site.register(Machine)
admin.site.register(UserMachine)
admin.site.register(Info)
admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(IncidentsMachine)
