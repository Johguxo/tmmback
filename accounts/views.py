import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Profile

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