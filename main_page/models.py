from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    genre_choices = (
        ("Комедия", "Комедия"),
        ("Драма", "Драма"),
        ("Ужасы", "Ужасы"),
        ("Романтика", "Романтика"),
    )
    image = models.ImageField(upload_to="books/", verbose_name="Загрузите обложку")
    title = models.CharField(max_length=100, verbose_name="Введите название книги")
    description = models.CharField(
        max_length=500, verbose_name="Введите описание книги", null=True
    )
    price = models.IntegerField(verbose_name="Введите цену")
    release_date = models.DateField(verbose_name="Введите дату выхода")
    genre = models.CharField(
        max_length=100, choices=genre_choices, verbose_name="Введите жанр", null=True
    )
    author_email = models.CharField(max_length=100, verbose_name="Введите email автора")
    author = models.CharField(max_length=100, verbose_name="Введите имя автора")
    review_link = models.URLField(
        verbose_name="Введите ссылку на обзор на youtube", null=True
    )

    def average_rating_of_last_5(self):
        reviews = self.review_books.order_by("-created_date")[:5]
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    def average_rating(self):
        reviews = self.review_books.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.title


class ReviewBooks(models.Model):
    review_books = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="review_books"
    )
    created_date = models.DateField(
        auto_now_add=True, null=True, verbose_name="Дата создания"
    )
    description = models.TextField(verbose_name="Оставьте отзыв о kниге", null=True)
    mark = models.PositiveIntegerField(
        verbose_name="Укажите оценку от 1 до 5",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        return f"{self.review_books}----{self.created_date}"
