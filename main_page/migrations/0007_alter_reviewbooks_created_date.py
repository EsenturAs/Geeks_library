# Generated by Django 5.1.2 on 2024-11-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_reviewbooks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbooks',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]