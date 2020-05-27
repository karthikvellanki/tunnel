import requests
import json
from django.db import models
from tunnelapp.models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import get_authorization_header, BasicAuthentication
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from requests.auth import HTTPBasicAuth
import base64


class Api(models.Model):
    PLUGIN_CHOICE_LIST = (
        (0, _('Remote auth')),
        (1, _('Key auth')),
        (2, _('Basic auth'))
    )
    UNIT_LIST = (
        ('s', 'Second'),
        ('m', 'Minute'),
        ('h', 'Hour'),
        ('d', 'Day')
    )
    name = models.CharField(max_length=128, unique=True)
    target_base_uri = models.CharField(max_length=128)
    api_name = models.CharField(max_length=255)
    authentication = models.IntegerField(choices=PLUGIN_CHOICE_LIST, default=0)
    anonthrottlevalue = models.CharField(max_length=128)
    anonthrottleunit = models.CharField(max_length=10, choices=UNIT_LIST, default=0)
    userthrottlevalue = models.CharField(max_length=128)
    userthrottleunit = models.CharField(max_length=10, choices=UNIT_LIST, default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
