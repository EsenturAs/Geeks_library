# Generated by Django 5.1.2 on 2024-11-29 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mobile_devices", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="devices",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices",
                to="mobile_devices.device",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="features",
            field=models.ManyToManyField(null=True, to="mobile_devices.feature"),
        ),
    ]
