import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(default="", max_length=200)
    model = models.CharField(default="", max_length=200)
    release_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.name} | {self.model}"
