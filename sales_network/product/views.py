from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsActive
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive)
