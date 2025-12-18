from django.forms import ModelForm, CheckboxInput, TextInput, SelectMultiple

from rss.models import Feed
from rss.widgets.date import DateInput


class FeedForm(ModelForm):
    template_name = "feed/form.html"

    class Meta:
        model = Feed
        fields = (
            "enabled",
            "name",
            "url",
            "regex_filter",
            "expires_at",
            "download_dir",
            "ignore_older_than",
            "ignore_newer_than",
            "start_paused",
            "chronological",
            "transmission_clients",
        )
        labels = {
            "enabled": "Enabled",
            "start_paused": "Start paused",
            "chronological": "Chronological",
            "transmission_clients": "Clients",
        }
        widgets = {
            "enabled": CheckboxInput(attrs={"class": "form-check-input"}),
            "name": TextInput(attrs={"class": "form-control"}),
            "url": TextInput(attrs={"class": "form-control"}),
            "regex_filter": TextInput(attrs={"class": "form-control"}),
            "expires_at": DateInput(attrs={"class": "form-control"}),
            "download_dir": TextInput(attrs={"class": "form-control"}),
            "ignore_older_than": DateInput(attrs={"class": "form-control"}),
            "ignore_newer_than": DateInput(attrs={"class": "form-control"}),
            "start_paused": CheckboxInput(attrs={"class": "form-check-input"}),
            "chronological": CheckboxInput(attrs={"class": "form-check-input"}),
            "transmission_clients": SelectMultiple(attrs={"class": "form-select"}),
        }
        help_texts = {
            "url": None,
            "regex_filter": None,
            "expires_at": None,
            "download_dir": None,
            "ignore_older_than": None,
            "ignore_newer_than": None,
            "start_paused": None,
            "chronological": None,
            "transmission_clients": None,
        }
