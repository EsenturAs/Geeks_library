# Generated by Django 5.1.2 on 2024-11-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_ranobelib', '0006_rename_chapter_ranobelib_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranobelib',
            old_name='genres',
            new_name='stat',
        ),
    ]