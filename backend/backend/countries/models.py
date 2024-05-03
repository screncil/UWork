from django.db import models

# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    image = models.URLField()

    @property
    def get_name(self):
        return str(self.name)

    def __str__(self):
        return self.name