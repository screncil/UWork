from django.db import models

from countries.models import Countries

# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
