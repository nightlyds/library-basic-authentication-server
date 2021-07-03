from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'updated_at', 'created_at', 'role',
        'is_active', 'password')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class AuthenticationLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=6, write_only=True, required=True)

    class Meta:
        fields = ('email', 'password')