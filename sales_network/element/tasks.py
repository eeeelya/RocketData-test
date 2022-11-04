import random

from celery import shared_task
from django.db.models import F
from rest_framework.generics import get_object_or_404

from element.models import Element


@shared_task
def increase_debt():
    element_for_increase = Element.objects.order_by("?").first()
    element_for_increase.debt_to_supplier = F("debt_to_supplier") + random.randint(0, 500)
    element_for_increase.save()


@shared_task
def reduce_debt():
    element_for_reduce = Element.objects.order_by("?").first()
    reduction_size = random.randint(100, 10000)

    if element_for_reduce.debt_to_supplier <= reduction_size:
        element_for_reduce.debt_to_supplier = 0
    else:
        element_for_reduce.debt_to_supplier = F("debt_to_supplier") - reduction_size

    element_for_reduce.save()


@shared_task
def admin_clear_debt(*args, **kwargs):
    element = get_object_or_404(Element, id=kwargs.get("id"))
    element.debt_to_supplier = 0.00
    element.save()
