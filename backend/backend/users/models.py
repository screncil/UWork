from django.contrib.auth.models import AbstractUser
from django.db import models

from countries.models import Countries
from cities.models import Cities


class User(AbstractUser):
    GENDERS = (
        ("M", "Мужчина"),
        ("F", "Женщина")
    )

    GROUPS = (
        ("company", "Компания"),
        ("user", "Пользователь")
    )

    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    img_url = models.ImageField(upload_to="images/", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    group = models.CharField(choices=GROUPS, blank=True, null=True)
    city = models.ForeignKey(Cities, blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.username