from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import ChangeEmailSerializer, ChangePasswordSerializer, TokenSerializer
import requests
import json
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
import datetime

User = get_user_model()


def get_user_from_token(request):
    key = request.META.get("HTTP_AUTHORIZATION").split(' ')[1]
    token = Token.objects.get(key=key)
    user = User.objects.get(id=token.user_id)
    return user


class UserEmailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        obj = {'email': user.email}
        return Response(obj)


class ChangeEmailView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        email_serializer = ChangeEmailSerializer(data=request.data)
        if email_serializer.is_valid():
            email = email_serializer.data.get('email')
            confirm_email = email_serializer.data.get('confirm_email')
            if email == confirm_email:
                user.email = email
                user.save()
                return Response({"email": email}, status=HTTP_200_OK)
            return Response({"message": "The emails did not match"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message": "Did not receive correct data"}, status=HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        password_serializer = ChangePasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            password = password_serializer.data.get('password')
            confirm_password = password_serializer.data.get('confirm_password')
            current_password = password_serializer.data.get('current_password')
            auth_user = authenticate(
                username=user.username,
                password=current_password
            )
            if auth_user is not None:
                if password == confirm_password:
                    auth_user.set_password(password)
                    auth_user.save()
                    return Response(status=HTTP_200_OK)
                else:
                    return Response({"message": "The passwords did not match"}, status=HTTP_400_BAD_REQUEST)
            return Response({"message": "Incorrect user details"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message": "Did not receive the correct data"}, status=HTTP_400_BAD_REQUEST)


class APIKeyView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        token_qs = Token.objects.filter(user=user)
        if token_qs.exists():
            token_serializer = TokenSerializer(token_qs, many=True)
            try:
                return Response(token_serializer.data, status=HTTP_200_OK)
            except:
                return Response({"message": "Did not receive correct data"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message": "User does not exist"}, status=HTTP_400_BAD_REQUEST)
