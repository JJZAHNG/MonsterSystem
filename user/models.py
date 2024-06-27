# user/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from member.models import MembershipLevel


class User(AbstractUser):
    phone_number = models.CharField(unique=True, verbose_name='手机号', max_length=11, default='00000000000')
    membership_level = models.ForeignKey(MembershipLevel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
