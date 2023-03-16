from django.contrib import admin
from machines.models import (Machine, UserMachine, 
      Info, Section,SubSection,IncidentsMachine)
# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    raw_id_fields = ('form',)
class UserMachineAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
class InfoAdmin(admin.ModelAdmin):
    raw_id_fields = ('section','subsection',)
class SectionAdmin(admin.ModelAdmin):
    raw_id_fields = ('machine',)
class SubSectionAdmin(admin.ModelAdmin):
    raw_id_fields = ('section',)

admin.site.register(Machine, MachineAdmin)
admin.site.register(UserMachine, UserMachineAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(SubSection, SubSectionAdmin)
admin.site.register(IncidentsMachine)
