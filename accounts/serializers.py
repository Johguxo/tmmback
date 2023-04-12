from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User
from accounts.models import Profile, UserAchievement
from machines.models import UserMachine
from datetime import datetime

class ProfileSerializer(ModelSerializer):
    """
      serializer section data
    """

    url_image = SerializerMethodField()
    url_signature = SerializerMethodField()
    data_user = SerializerMethodField()
    age = SerializerMethodField()
    role = SerializerMethodField()
    level = SerializerMethodField()
    specialist = SerializerMethodField()
    achievements = SerializerMethodField()
    machines = SerializerMethodField()


    class Meta:
        model = Profile
        fields = ('id','data_user','url_image', 'url_signature', 'role', 
                  'date_of_birth', 'code', 'level', 'achievements', 'machines',
                  'date_of_admission', 'specialist','objectives','age')
        

    def get_role(self,obj):
       return obj.get_role_display()

    def get_specialist(self,obj):
       return obj.get_specialist_display()
    
    def get_level(self,obj):
       return obj.get_level_display()

    def get_data_user(self, obj):
       data_user = None
       if obj.user:
          data_user = {
             'id': obj.user.id,
             'full_name': obj.user.get_full_name()
          }
       return data_user
    def get_url_image(self,obj):
        url_image = None
        if obj.image:
          url_image = f"https://res.cloudinary.com/johguxo-gonzales/{obj.image}"
        return url_image

    def get_url_signature(self,obj):
        url_signature = None
        if obj.signature:
          url_signature = f"https://res.cloudinary.com/johguxo-gonzales/{obj.signature}"
        return url_signature

    def get_age(self, obj):
      calculate_age = 1
      if obj.date_of_birth:
        calculate_age = datetime.now().year - obj.date_of_birth.year
      return calculate_age
   
    def get_achievements(self,obj):
       achievements = []
       if UserAchievement.objects.filter(user=obj.user).exists():
          for user_achievement in UserAchievement.objects.filter(user=obj.user):
             achievements.append({
                'name': user_achievement.achievement.name
             })
       return achievements
    def get_machines(self, obj):
       machines = []
       if UserMachine.objects.filter(user=obj.user).exists():
          for user_machine in UserMachine.objects.filter(user=obj.user):
             machines.append({
                'title': user_machine.machine.title
             })
       return machines

class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = '__all__'