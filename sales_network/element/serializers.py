from rest_framework import serializers

from element.models import Element, ElementEmployees, ElementProducts


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = "__all__"
        read_only_fields = ("debt_to_supplier", "created_at")


class ElementProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementProducts
        fields = "__all__"


class ElementEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementEmployees
        fields = "__all__"


class QrCodeSserializer(serializers.Serializer):
    id = serializers.CharField()
