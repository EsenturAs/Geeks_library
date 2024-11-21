from django.db import models


class Ranobelib(models.Model):
    title = models.CharField(max_length=900)
    stat = models.CharField(max_length=900, null=True)
    description = models.CharField(max_length=900, null=True)
    image = models.ImageField(upload_to="parser/image")

    def __str__(self):
        return self.title
