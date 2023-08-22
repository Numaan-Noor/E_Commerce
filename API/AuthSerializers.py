from rest_framework import serializers
from .models import UserLogin

class AuthCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
