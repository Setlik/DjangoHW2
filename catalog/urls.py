from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ContactView,
    ProductDetailView,
    ProductCreateView,
    ProductEditView,
    ProductDelete,
    ProductUnpublish,
)
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/edit/<int:pk>/", ProductEditView.as_view(), name="product_edit"),
    path(
        "product/<int:product_id>/delete/",
        ProductDelete.as_view(),
        name="delete_product",
    ),  # Удаление продукта
    path(
        "product/<int:product_id>/unpublish/",
        ProductUnpublish.as_view(),
        name="unpublish_product",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
