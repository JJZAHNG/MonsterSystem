from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(unique=True, verbose_name='手机号', blank=True, null=True, max_length=11)
