from django.conf.urls.static import static
from django.conf import settings
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('login-api/', views.AuthenticateUserAPI.as_view()),
    path('home/', views.index,name='index')
    #path('register-api/', views.RegisterUserAPI.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)