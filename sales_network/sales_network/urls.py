"""sales_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from core.login_view import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("register/", UserViewSet.as_view({"post": "create"}), name="register"),
    path("login/", LoginView.as_view(), name="login"),

    path("api/v1/", include("element.urls")),
    path("api/v1/", include("product.urls")),
]
