# Generated by Django 5.1.2 on 2024-11-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0005_reviewbooks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewbooks",
            name="description",
            field=models.TextField(null=True, verbose_name="Оставьте отзыв о kниге"),
        ),
    ]
