from django.db import models

from countries.models import Countries

# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
