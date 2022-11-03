from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg


from core.permissions import IsActive
from element.serializers import (
    ElementSerializer,
    ElementProductsSerializer,
    ElementEmployeesSerializer,
)
from element.models import Element, ElementProducts, ElementEmployees
from element.filters import ElementSearchFilter


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = (IsActive,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ElementSearchFilter

    @action(detail=False, methods=["get"])
    def large_debtors(self, request):
        debt = self.queryset.aggregate(average=Avg("debt_to_supplier"))
        serializer = self.get_serializer(
            self.queryset.filter(debt_to_supplier__gte=debt["average"]), many=True
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class ElementProductsViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ElementProducts.objects.all()
    serializer_class = ElementProductsSerializer


class ElementEmployeesViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ElementEmployees.objects.all()
    serializer_class = ElementEmployeesSerializer
