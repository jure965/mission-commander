from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("mission_commander.rss.urls")),
    path("admin/", admin.site.urls),
]
