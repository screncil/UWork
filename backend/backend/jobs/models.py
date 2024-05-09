from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField

from categories.models import Category
from users.models import User
from countries.models import Countries
from cities.models import Cities


# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    requirements = ArrayField(models.TextField(), default=list)
    offer = ArrayField(models.TextField(), default=list)
    salary = models.IntegerField()
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, default=None, null=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, default=None, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title