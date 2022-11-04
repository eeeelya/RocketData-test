import datetime

from django.db import models
from django.core.exceptions import ValidationError


def date_existing(value):
    if value > datetime.date.today():
        raise ValidationError("The release date can't be in the future!")
    return value


class Product(models.Model):
    name = models.CharField(default="", max_length=25)
    model = models.CharField(default="", max_length=50)
    release_date = models.DateField(default=datetime.date.today, validators=[date_existing])

    def __str__(self):
        return f"{self.name} | {self.model}"
