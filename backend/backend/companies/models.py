from django.db import models

from countries.models import Countries
from cities.models import Cities

# Create your models here.


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)


    def __str__(self):
        return self.name