# Generated by Django 5.0.6 on 2024-05-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issues", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Opened"), (2, "In progress"), (3, "Closed")]
            ),
        ),
        migrations.DeleteModel(
            name="Message",
        ),
    ]
