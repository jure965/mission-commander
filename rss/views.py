from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView


class FeedListView(TemplateView):
    template_name = "rss/feed_list.html"


class TorrentListView(TemplateView):
    template_name = "rss/torrent_list.html"


class ClientListView(TemplateView):
    template_name = "rss/client_list.html"


class LoginView(TemplateView):
    template_name = "rss/login.html"

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        return super().get(request)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")
