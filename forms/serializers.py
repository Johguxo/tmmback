from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User
from forms.models import Form, Questions, Choices, Responses


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
  validate_response = SerializerMethodField()

  class Meta:
    model = Form
    fields = ('code','title','description','creator','background_color', 'text_color',
              'collect_email', 'authenticated_responder','edit_after_submit',
              'confirmation_message','is_quiz','allow_view_score','questions',
              'createdAt','updatedAt','validate_response')
  
  def get_validate_response(self, obj):
    if 'id_user' in self.context['request'].GET:
        id_user = self.context['request'].GET['id_user']
        user = User.objects.get(id=id_user)
        if Responses.objects.filter(responder=user,
                                    response_to=obj).exists():
          return True
    return False
  
    
