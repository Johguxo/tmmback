from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User
from machines.models import Machine, Section, SubSection, Info


class MachineSerializer(ModelSerializer):
    """
      get machine data
    """
    url_image = SerializerMethodField()
    code_form = SerializerMethodField()

    class Meta:
        model = Machine
        fields = ('id','title','code_form','description','url_image')
    
    def get_url_image(self, obj):
        url_image = None
        if obj.image:
          url_image = f"https://res.cloudinary.com/johguxo-gonzales/{obj.image}"
        return url_image
    def get_code_form(self, obj):
        code_form = None
        if obj.form:
          code_form = obj.form.code
        return code_form


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

class InfoSerializer(ModelSerializer):
    """
      serializer section data
    """
    url_image = SerializerMethodField()

    class Meta:
        model = Info
        fields = ('id','title','subtitle','content','url_image','video_link')

    def get_url_image(self, obj):
        url_image = None
        if obj.image:
          url_image = f"https://res.cloudinary.com/johguxo-gonzales/{obj.image}"
        return url_image