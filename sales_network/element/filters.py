from django.contrib import admin
from django.utils.translation import gettext_lazy as _


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
