# member/models.py

from django.db import models


class MembershipLevel(models.Model):
    LEVEL_CHOICES = [
        ('Junior Basic', '初级 基础'),
        ('Junior Plus', '初级 进阶'),
        ('Junior Ultra', '初级 强化'),
        ('Intermediate Basic', '中级 基础'),
        ('Intermediate Plus', '中级 进阶'),
        ('Intermediate Ultra', '中级 强化'),
        ('Senior Basic', '高级 基础'),
        ('Senior Plus', '高级 进阶'),
        ('Senior Ultra', '高级 强化'),
    ]

    name = models.CharField(max_length=20, choices=LEVEL_CHOICES, unique=True)
    skill_training = models.IntegerField()
    problem_solving = models.IntegerField()
    competition_guidance = models.IntegerField()
    camp = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
