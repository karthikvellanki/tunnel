from django.urls import path
from .views import (ChangeEmailView, UserEmailView, ChangePasswordView, APIKeyView)

app_name = 'tunnelapp'

urlpatterns = [
    path('email/', UserEmailView.as_view(), name='email'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api-key/', APIKeyView.as_view(), name='api-key'),
]
