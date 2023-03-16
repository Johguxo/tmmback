from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User
from forms.models import Form, Questions, Choices


class ChoicesSerializer(ModelSerializer):
  """
    Seralizer Choices data
  """

  class Meta:
    model = Choices
    fields = '__all__'


class QuestionSerializer(ModelSerializer):
  """
    Serializer Questions data
  """
  
  choices = ChoicesSerializer(many=True)

  class Meta:
    model = Questions
    fields = '__all__'

class FormSerializer(ModelSerializer):
  """
    Serializer form data
  """

  questions = QuestionSerializer(many=True)

  class Meta:
    model = Form
    fields = '__all__'
    
