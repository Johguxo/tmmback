from django.contrib import admin
from accounts.models import (Profile)

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)