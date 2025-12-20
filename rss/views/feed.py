import json
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from rss.forms import FeedForm
from rss.models import Feed

from rss.tasks import fetch_feeds

logger = logging.getLogger(__name__)


class FeedListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "feed/list.html"
    model = Feed
    context_object_name = "feeds"


class FeedCreateView(LoginRequiredMixin, CreateView):
    template_name = "feed/create.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        feed: Feed = self.object
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.MINUTES,
        )
        feed.periodic_task = PeriodicTask.objects.create(
            interval=schedule,
            name=f"rss.parse_feed.{feed.id}",
            task="rss.tasks.parse_feed",
            kwargs=json.dumps({"feed_id": feed.id}),
            enabled=True,
        )
        feed.save()
        return response


class FeedUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "feed/update.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")


class FeedDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "feed/delete.html"
    model = Feed
    success_url = reverse_lazy("feed-list")


class FeedCheckView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, *args, **kwargs):
        fetch_feeds.delay()
        return redirect("feed-list")
