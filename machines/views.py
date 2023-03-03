from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from machines.models import Machine, UserMachine, Section, SubSection
from machines.serializers import MachineSerializer, SectionSerializer, SubSectionSerializer

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
            return Section.objects.filter(machine_id=self.request.GET['id_machine'])
        return ModelViewSet.get_queryset(self)

class SubSectionAPI(ModelViewSet):
    """
      Get sections of machine
    """
    permission_classes = [AllowAny]
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        if 'id_section' in self.request.GET:
            return SubSection.objects.filter(section_id=self.request.GET['id_section'])
        return ModelViewSet.get_queryset(self)