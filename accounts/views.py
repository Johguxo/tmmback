import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from accounts.models import Profile
from .forms import NewUserForm

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

logger = logging.getLogger('login_logger')

class AuthenticateUserAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """ Post method for the authentication of a user """
        context = {'request': request}
        email = request.data['email']
        password = request.data['password']
        obj_user = None
        user = None
        is_authenticated = False
        response_error_dict = {'status': False, 'app': {'status': False}}
        if User.objects.filter(email=email, is_active=True).exists():
          obj_user = User.objects.filter(email=email, is_active=True).last()
          user = authenticate(username=obj_user.username,
                                password=password)
          print(user)
        return Response(response_error_dict)


def register(request):
  """ View function for home page of site """
  
  context = {
    'num_machines': 5,
  }

  if request.method == "POST":
    formData = {
      'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
      'username': request.POST['code'],
      'email': request.POST['email'],
      'first_name': request.POST['first_name'],
      'last_name': request.POST['last_name'],
      'password1': request.POST['password1'],
      'password2': request.POST['password2']
    }
    form = NewUserForm(formData)
    if form.is_valid():
      user = form.save()
      Profile.objects.create(user=user,code=request.POST['code'])
      login(request,user)
      messages.success(request, "Registration successful." )
      return redirect("homepage")
    messages.error(request, "Unsuccessful registration. Invalid information.")

  return render(request, 'register.html', context=context)


def home(request):
   return render(request, 'home.html')