# Generated by Django 4.2.1 on 2024-09-03 09:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="users",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]