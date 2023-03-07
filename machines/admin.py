from django.contrib import admin
from machines.models import (Machine, UserMachine, 
      Info, Section,SubSection,IncidentsMachine)
# Register your models here.

class UserMachineAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
class InfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('section','subsection',)
class SectionAdmin(admin.ModelAdmin):
    raw_id_fields = ('machine',)
class SubSectionAdmin(admin.ModelAdmin):
    raw_id_fields = ('section',)
class IncidentsMachineAdmin(admin.ModelAdmin):
    raw_id_fields = ('machine',)

admin.site.register(Machine)
admin.site.register(UserMachine, UserMachineAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SubSection, SubSectionAdmin)
admin.site.register(IncidentsMachine, IncidentsMachineAdmin)
