from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone

import datetime

# Created to extend the User functionality in the future


class User(AbstractUser):
    is_user = models.BooleanField(default=True)
