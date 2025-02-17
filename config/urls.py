from django.contrib import admin
from django.urls import path, include

from users.views import register, login_view, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
    path("blog/", include("blog.urls")),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
