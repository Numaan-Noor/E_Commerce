from rest_framework import serializers
from .models import UserLogin

# class AuthCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserLogin
#         fields = '__all__'

class AuthCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ('id', 'Name', 'email','PhoneNumber', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserLogin.objects.create_user(**validated_data)
        return user