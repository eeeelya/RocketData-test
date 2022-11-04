import random

import factory.fuzzy
from faker import Faker

from element.models import Element, ElementProducts


def random_element_object_selection():
    queryset = Element.objects.all()

    if len(queryset):
        return queryset[random.randint(0, len(queryset) - 1)]


def random_contacts():
    countries = ("Belarus", "Poland", "Latvia")
    cities = ("Minsk", "Warsaw", "Riga")

    return {
        "email": "element@gmail.com",
        "address": {
            "country": countries[random.randint(0, 2)],
            "city": cities[random.randint(0, 2)],
            "street": "Prigorodnaya",
            "house_number": "1",
        },
    }


class ElementFactory(factory.django.DjangoModelFactory):
    type = factory.fuzzy.FuzzyChoice(choices=Element.Type.choices, getter=lambda c: c[0])
    name = factory.Sequence(lambda n: "element-%d" % n)
    contacts = factory.LazyFunction(random_contacts)
    parent = factory.LazyFunction(random_element_object_selection)
    debt_to_supplier = factory.Faker("pydecimal", left_digits=8, right_digits=2, positive=True)

    class Meta:
        model = Element
