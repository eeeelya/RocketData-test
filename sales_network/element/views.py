from rest_framework import viewsets, mixins, status, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
from element.serializers import QrCodeSserializer
from element.tasks import send_qrcode_on_email


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    permission_classes = (IsAuthenticated, IsActive)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ElementSearchFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Element.objects.all()
        else:
            return Element.objects.filter(employees__in=[self.request.user])

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
    permission_classes = (IsAuthenticated,)


class ElementEmployeesViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ElementEmployees.objects.all()
    serializer_class = ElementEmployeesSerializer
    permission_classes = (IsAuthenticated,)


class QrCodeApiView(views.APIView):
    def post(self, request):
        serializer = QrCodeSserializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_qrcode_on_email.delay(id=serializer.data["id"], user_email=request.user.email)

        return Response(serializer.data, status=status.HTTP_200_OK)
