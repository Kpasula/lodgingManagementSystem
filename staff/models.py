from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    shift = models.CharField(max_length=10, default=' ', null=True, blank=True)
    staff_phone = models.CharField(max_length=10, default=' ', null=True, blank=True)
