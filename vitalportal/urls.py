from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("vitals/", include("vitals.urls")),
    path("mood/", include("mood.urls")),
]
