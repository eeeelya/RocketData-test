import factory

from element.models import Element, ElementEmployees
from core.factories.user_model import UserFactory


class ElementEmployeesFactory(factory.django.DjangoModelFactory):
    element = factory.Iterator(Element.objects.all())
    employee = factory.SubFactory(UserFactory)

    class Meta:
        model = ElementEmployees
