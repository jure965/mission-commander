from django.forms import ModelForm, DateTimeInput

from mission_commander.rss.models import Feed
from mission_commander.rss.widgets import CheckboxInput


class FeedForm(ModelForm):
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
            "enabled": "",
            "start_paused": "",
            "chronological": "",
            "transmission_clients": "Clients",
        }
        widgets = {
            "enabled": CheckboxInput(label="Enabled"),
            "start_paused": CheckboxInput(label="Start paused"),
            "chronological": CheckboxInput(label="Chronological"),
            "expires_at": DateTimeInput(attrs={"class": "flatpickr"}),
            "ignore_older_than": DateTimeInput(attrs={"class": "flatpickr"}),
            "ignore_newer_than": DateTimeInput(attrs={"class": "flatpickr"}),
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
