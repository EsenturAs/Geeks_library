from django.db import models
from main_page.models import Book


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Введите Ваше имя")
    phone_number = models.IntegerField(verbose_name="Введите Ваш номер телефона", null=True)
    email = models.EmailField(max_length=100, verbose_name="Введите Ваш имейл")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='order_books', verbose_name="Выберите книгу")

    def __str__(self):
        return f"{self.name} - {self.name} - {self.phone_number}"
