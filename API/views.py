from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserLogin
from .AuthSerializers import AuthCreateSerializer
from rest_framework import status
class AuthSignUp(viewsets.ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = AuthCreateSerializer

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = AuthCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)