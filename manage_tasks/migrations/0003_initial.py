# Generated by Django 4.0.3 on 2022-03-17 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manage_tasks', '0002_initial'),
    ]

    operations = [

    ]
