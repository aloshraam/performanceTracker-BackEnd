# Generated by Django 4.2.5 on 2025-04-08 09:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrapi", "0006_projects_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="participants",
            field=models.ManyToManyField(
                related_name="meetings", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
