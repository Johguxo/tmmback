from django.contrib import admin
from accounts.models import (Profile,Achievement,Skill,UserAchievement,UserSkill)

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
class UserAchievementAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
class UserSkilleAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Achievement)
admin.site.register(Skill)
admin.site.register(UserAchievement, UserAchievementAdmin)
admin.site.register(UserSkill, UserSkilleAdmin)