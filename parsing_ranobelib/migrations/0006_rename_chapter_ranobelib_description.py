# Generated by Django 5.1.2 on 2024-11-21 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_ranobelib', '0005_rename_time_ranobelib_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranobelib',
            old_name='chapter',
            new_name='description',
        ),
    ]
