# Generated by Django 5.1.2 on 2024-11-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_ranobelib', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranobelib',
            name='chapter',
        ),
        migrations.AddField(
            model_name='ranobelib',
            name='rating',
            field=models.CharField(max_length=900, null=True),
        ),
    ]
