from django.db import models


class Book(models.Model):
    genre_choices = (
        ("Комедия", "Комедия"),
        ("Драма", "Драма"),
        ("Ужасы", "Ужасы"),
        ("Романтика", "Романтика"),
    )
    image = models.ImageField(upload_to="books/", verbose_name="Загрузите обложку")
    title = models.CharField(max_length=100, verbose_name="Введите название книги")
    description = models.CharField(max_length=500, verbose_name="Введите описание книги", null=True)
    price = models.IntegerField(verbose_name="Введите цену")
    release_date = models.DateField(verbose_name="Введите дату выхода")
    genre = models.CharField(max_length=100, choices=genre_choices, verbose_name="Введите жанр", null=True)
    author_email = models.CharField(max_length=100, verbose_name="Введите email автора")
    author = models.CharField(max_length=100, verbose_name="Введите имя автора")
    review_link = models.URLField(verbose_name="Введите ссылку на обзор на youtube", null=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
