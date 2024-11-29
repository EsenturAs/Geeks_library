from django.db import models
from django.contrib.auth.models import User


class Developer(User):
    QUALIFICATION_CHOICES = (
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    )

    qualification = models.CharField(
        max_length=30, choices=QUALIFICATION_CHOICES, default="None"
    )
    salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.qualification == "Junior":
            self.salary = 300
        elif self.qualification == "Middle":
            self.salary = 1000
        elif self.qualification == "Senior":
            self.salary = 2000
        else:
            self.salary = 0

        super().save(*args, **kwargs)
