from django.db import models


class Age(models.Model):
    age = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.age


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=100)
    tags = models.ManyToManyField(Age)

    def __str__(self):
        return self.title
