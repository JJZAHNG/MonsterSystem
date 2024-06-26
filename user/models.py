# user/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(unique=True, verbose_name='手机号', max_length=11)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']  # 必须包含username字段，否则createsuperuser会报错
