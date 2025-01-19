from django.contrib import admin
from django.urls import path, include

from catalog.views import product_detail, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("", home, name="home"),
]
