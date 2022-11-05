import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    email = factory.Faker("email")
    is_staff = factory.Faker("pybool")
    is_active = factory.Faker("pybool")

    class Meta:
        model = User
