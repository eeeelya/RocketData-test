from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from element.models import Element, ElementEmployees, ElementProducts
from element.filters import CityFilter
from element.tasks import admin_clear_debt


class ElementAdmin(DraggableMPTTAdmin):
    list_display = ("tree_actions", "indented_title", "parent")
    list_display_links = ("indented_title", "parent")
    list_filter = (CityFilter, )
    readonly_fields = ("created_at",)
    actions = ("clear_debt",)

    @admin.action(description="Clear the debt to the supplier")
    def clear_debt(self, request, queryset):
        if len(queryset) < 20:
            queryset.update(debt_to_supplier=0.00)
        else:
            for query in queryset:
                admin_clear_debt.delay(id=query.id)


admin.site.register(Element, ElementAdmin)
admin.site.register(ElementProducts)
admin.site.register(ElementEmployees)
