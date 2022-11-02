from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from element.models import Element, ElementEmployees, ElementProducts
from element.filters import CityFilter


class ElementAdmin(DraggableMPTTAdmin):
    list_display = ("tree_actions", "indented_title", "parent")
    list_display_links = ("indented_title", "parent")
    list_filter = (CityFilter, )
    readonly_fields = ("created_at",)
    actions = ("clear_debt",)

    @admin.action(description="Clear the debt to the supplier")
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0.00)


admin.site.register(Element, ElementAdmin)
admin.site.register(ElementProducts)
admin.site.register(ElementEmployees)
