# Generated by Django 5.0.6 on 2024-05-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
