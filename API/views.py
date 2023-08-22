from django.shortcuts import render
from rest_framework import viewsets
from .models import UserLogin
from .AuthSerializers import AuthCreateSerializer

class AuthSignUp(viewsets.ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = AuthCreateSerializer

