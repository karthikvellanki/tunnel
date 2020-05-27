from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls import url
from gateway.views import gateway
from tunnelapp import views

urlpatterns = [
    path('', include('frontend.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('tunnelapp.urls', namespace='api')),
    url(r'^service/', gateway.as_view(), name='gateway')
]
