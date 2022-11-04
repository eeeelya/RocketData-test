import factory
from factory.django import DjangoModelFactory

from product.models import Product


class ProductFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "name-%d" % n)
    model = factory.Sequence(lambda n: "model-%d" % n)
    release_date = factory.Faker('date_object')

    class Meta:
        model = Product
