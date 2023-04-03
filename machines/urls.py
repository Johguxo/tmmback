from rest_framework.routers import DefaultRouter
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.MachineAPI.as_view({'get': 'list'})),
    re_path(r'^(?P<id>[0-9]+)/$', views.MachineAPI.as_view({'get': 'retrieve'})),
    re_path(r'^section-api/$', views.SectionAPI.as_view({'get': 'list'})),
    re_path(r'^subsection-api/$', views.SubSectionAPI.as_view({'get': 'list'})),
    re_path(r'^info-api/$', views.InfoAPI.as_view({'get': 'list'})),
    re_path(r'^info-api/(?P<id>[0-9]+)/$', views.InfoAPI.as_view({'get': 'retrieve'})),
    re_path(r'^incidents-api/$', views.IncidentsAPÏ.as_view({'get': 'list'})),
    #re_path(r'^/$', views.MachineAPI.as_view())
]