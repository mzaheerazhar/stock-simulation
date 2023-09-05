from .base import BaseModel
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.core.validators import EmailValidator
from django.db import models


class User(AbstractUser, BaseModel, PermissionsMixin):
    username = models.CharField(max_length=50,  unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField(default=100000)
