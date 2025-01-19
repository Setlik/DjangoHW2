from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact, product_detail
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contacts"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)