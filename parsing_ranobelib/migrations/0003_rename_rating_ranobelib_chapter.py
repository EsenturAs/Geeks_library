# Generated by Django 5.1.2 on 2024-11-21 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_ranobelib', '0002_remove_ranobelib_chapter_ranobelib_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranobelib',
            old_name='rating',
            new_name='chapter',
        ),
    ]