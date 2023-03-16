from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileSerializer(ModelSerializer):
    """
      serializer section data
    """

    class Meta:
        model = Profile
        fields = '__all__'