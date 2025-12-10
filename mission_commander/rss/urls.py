from django.urls import path

from mission_commander.rss.views import (
    FeedListView,
    FeedCreateView,
    FeedUpdateView,
    FeedDeleteView,
    ClientListView,
    ClientCreateView,
    LoginView,
    LogoutView,
    ClientUpdateView,
    ClientDeleteView,
    TorrentListView,
    TorrentDetailView,
    OnceCreateView,
    FeedCheckView,
)

urlpatterns = [
    path("", FeedListView.as_view(), name="feed-list"),
    path("once/", OnceCreateView.as_view(), name="once-add"),
    path("feed/add/", FeedCreateView.as_view(), name="feed-add"),
    path("feed/check/", FeedCheckView.as_view(), name="feed-check"),
    path("feed/<int:pk>/", FeedUpdateView.as_view(), name="feed-update"),
    path("feed/<int:pk>/delete/", FeedDeleteView.as_view(), name="feed-delete"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/add/", ClientCreateView.as_view(), name="client-add"),
    path("client/<int:pk>/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("torrent/", TorrentListView.as_view(), name="torrent-list"),
    path("torrent/<int:pk>/", TorrentDetailView.as_view(), name="torrent-detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
