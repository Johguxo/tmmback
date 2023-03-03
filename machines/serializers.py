from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from django.contrib.auth.models import User
from machines.models import Machine, Section, SubSection



class MachineSerializer(ModelSerializer):
    """
      get machine data
    """
    class Meta:
        model = Machine
        fields = '__all__'


class SectionSerializer(ModelSerializer):
    """
      serializer section data
    """

    class Meta:
        model = Section
        fields = '__all__'

class SubSectionSerializer(ModelSerializer):
    """
      serializer section data
    """

    class Meta:
        model = SubSection
        fields = '__all__'