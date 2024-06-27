# Generated by Django 3.2.22 on 2024-06-27 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='assistants',
            field=models.ManyToManyField(blank=True, to='course.Assistant'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursetype'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.instructor'),
        ),
    ]
