from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDERS = (
        ("M", "Мужчина"),
        ("F", "Женщина")
    )

    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username