from django.contrib import admin
from django.urls import path

from rss.views import (
    FeedListView,
    TorrentListView,
    ClientListView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path("", FeedListView.as_view()),
    path("torrent/", TorrentListView.as_view()),
    path("client/", ClientListView.as_view()),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]
