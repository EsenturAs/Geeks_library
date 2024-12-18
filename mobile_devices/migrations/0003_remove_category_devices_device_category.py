# Generated by Django 5.1.2 on 2024-11-29 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mobile_devices", "0002_category_devices_device_features"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="devices",
        ),
        migrations.AddField(
            model_name="device",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices",
                to="mobile_devices.category",
            ),
        ),
    ]
