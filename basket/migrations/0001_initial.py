# Generated by Django 5.1.2 on 2024-11-15 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main_page", "0007_alter_reviewbooks_created_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Введите Ваше имя"),
                ),
                (
                    "phone_number",
                    models.IntegerField(
                        max_length=100, verbose_name="Введите Ваш номер телефона"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=100, verbose_name="Введите Ваш имейл"),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_books",
                        to="main_page.book",
                        verbose_name="Выберите книгу",
                    ),
                ),
            ],
        ),
    ]
