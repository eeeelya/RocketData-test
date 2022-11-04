import factory

from element.models import Element, ElementProducts
from product.factories.product_model import ProductFactory


class ElementProductsFactory(factory.django.DjangoModelFactory):
    element = factory.Iterator(Element.objects.all())
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = ElementProducts
