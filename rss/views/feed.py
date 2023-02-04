from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rss.forms import FeedForm
from rss.models import Feed


class FeedListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "rss/feed/list.html"
    model = Feed
    context_object_name = "feeds"


class FeedCreateView(LoginRequiredMixin, CreateView):
    template_name = "rss/feed/create.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")


class FeedUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "rss/feed/update.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")


class FeedDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "rss/feed/delete.html"
    model = Feed
    success_url = reverse_lazy("feed-list")
