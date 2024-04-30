from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    image = models.URLField()

    def __str__(self):
        return self.name