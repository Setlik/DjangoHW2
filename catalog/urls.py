from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)