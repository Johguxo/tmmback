from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from machines.models import Machine, Info, UserMachine, Section, SubSection, Incidents
from machines.serializers import MachineSerializer, InfoSerializer, SectionSerializer, SubSectionSerializer, IncidentsSerializer

class MachineAPI(ModelViewSet):
    """
      Get all machines
    """
    permission_classes = [AllowAny]
    serializer_class = MachineSerializer
    queryset = Machine.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Machine.objects.all()
        if 'id_user' in self.request.GET:
            queryset = UserMachine.objects.filter(user_id=self.request.GET['id_user'])
            return queryset
        return ModelViewSet.get_queryset(self)
  
class UserMachineAPI(APIView):
    """
      Get all machines
    """
    def get(self, request):
        if 'id_machine' in request.GET:
            request.GET['id_machine']
  

class SectionAPI(ModelViewSet):
    """
      Get sections of machine
    """
    permission_classes = [AllowAny]
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        if 'id_machine' in self.request.GET:
            queryset = Section.objects.filter(machine_id=self.request.GET['id_machine'])
            print(queryset)
            return queryset
        return ModelViewSet.get_queryset(self)

class SubSectionAPI(ModelViewSet):
    """
      Get sub sections of machine
    """
    permission_classes = [AllowAny]
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        if 'id_section' in self.request.GET:
            return SubSection.objects.filter(section_id=self.request.GET['id_section'])
        return ModelViewSet.get_queryset(self)
    
  
class InfoAPI(ModelViewSet):
    """
      Get info of section or subsection
    """
    permission_classes = [AllowAny]
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        if 'type' in self.request.GET and 'id_model' in self.request.GET:
            id_model = self.request.GET['id_model']
            type = self.request.GET['type']
            if type == 'section':
              query = Info.objects.filter(section_id=id_model)
            else:
              query = Info.objects.filter(subsection_id=id_model)
            return query
        return ModelViewSet.get_queryset(self)

class IncidentsAPÏ(ModelViewSet):
    """
      Get info of incidents
    """
    permission_classes = [AllowAny]
    serializer_class = IncidentsSerializer
    queryset = Incidents.objects.all()
    lookup_field = 'id'