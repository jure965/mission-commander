from django.views.generic import TemplateView


class FeedListView(TemplateView):
    template_name = "rss/feed_list.html"
