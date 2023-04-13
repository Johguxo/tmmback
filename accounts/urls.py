from django.conf.urls.static import static
from django.conf import settings
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('authtenticate-login/', views.AuthenticateUserAPI.as_view()),
    path('login', views.login_view, name="login"),
    path('register/', views.register,name='register'),
    path('logout', views.logout_view, name="logout"),
    path('home/', views.home,name='homepage'),
    path('get_profiles/', views.ProfileAPI.as_view({'get': 'list'}), name='get_profiles')
    #path('register-api/', views.RegisterUserAPI.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)