from django.db.models import Q
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, CharFilter, filters

from element.models import Element


class CityFilter(admin.SimpleListFilter):
    title = _("City filter")
    parameter_name = "city"

    def lookups(self, request, model_admin):
        unique_cities = set()

        for el in model_admin.get_queryset(request):
            unique_cities.add(
                (el.contacts["address"]["city"], el.contacts["address"]["city"])
            )

        return unique_cities

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        return queryset.filter(contacts__address__city=self.value())


class ElementSearchFilter(FilterSet):
    country = filters.CharFilter(method="country_filter", field_name="Country filter")
    product_id = filters.NumberFilter(field_name="products__id")

    class Meta:
        model = Element
        fields = ("country", "product_id")

    def country_filter(self, queryset, name, value):
        return Element.objects.filter(Q(contacts__address__country=value))
