from django.contrib import admin
from django.urls import path

from rss.views import (
    FeedListView,
    TorrentListView,
    ClientListView,
    ClientCreateView,
    LoginView,
    LogoutView,
    ClientUpdateView,
    ClientDeleteView,
)

urlpatterns = [
    path("", FeedListView.as_view(), name="feed-list"),
    path("torrent/", TorrentListView.as_view(), name="torrent-list"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/add/", ClientCreateView.as_view(), name="client-add"),
    path("client/<int:pk>/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
]
