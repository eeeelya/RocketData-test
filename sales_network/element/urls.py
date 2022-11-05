from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from element.views import ElementViewSet, ElementProductsViewSet, ElementEmployeesViewSet, QrCodeApiView

router = DefaultRouter()
router.register(r"element", ElementViewSet, basename="element")
router.register(r"element-products", ElementProductsViewSet, basename="element_products")
router.register(r"element-employees", ElementEmployeesViewSet, basename="element_employees")

urlpatterns = [
    path("", include(router.urls)),

    path("element-qrcode/", QrCodeApiView.as_view()),
    path("element-button/", TemplateView.as_view(template_name="elements_button.html")),
]
