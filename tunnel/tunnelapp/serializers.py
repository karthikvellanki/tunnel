from rest_framework import serializers
from rest_framework.authtoken.models import Token


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirm_email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input-type': 'password'})
    confirm_password = serializers.CharField(style={'input-type': 'password'})
    current_password = serializers.CharField(style={'input-type': 'password'})


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('pk', 'key')
