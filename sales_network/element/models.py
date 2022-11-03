import datetime

from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

from product.models import Product


def get_default_contacts():
    return {
        "email": "",
        "address": {
            "country": "",
            "city": "",
            "street": "",
            "house_number": "",
        },
    }


class Element(MPTTModel):
    class Type(models.IntegerChoices):
        FACTORY = 0
        DISTRIBUTOR = 1
        DEALERSHIP = 2
        RETAIL = 3
        IE = 4

    type = models.IntegerField(choices=Type.choices, default=Type.FACTORY)
    name = models.CharField(default="", max_length=200)
    contacts = models.JSONField(default=get_default_contacts)
    products = models.ManyToManyField(Product, through="ElementProducts")
    employees = models.ManyToManyField(User, through="ElementEmployees")
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    debt_to_supplier = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name} | {self.type}"

    def save(self, *args, **kwargs):
        if self.type == 0:
            self.parent = None
            super(Element, self).save(*args, **kwargs)
        else:
            if self.parent.type >= self.type:
                raise ValueError("You can't add parent with a lower level in the hierarchy.")
            else:
                super(Element, self).save(*args, **kwargs)


class ElementProducts(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "element_products"

    def __str__(self):
        return f"{self.element.name} | {self.product.name}"


class ElementEmployees(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "element_employees"

    def __str__(self):
        return f"{self.element.name} | {self.employee.name}"
