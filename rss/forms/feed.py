from django.forms import (
    ModelForm,
    CheckboxInput,
    TextInput,
    SelectMultiple,
    BooleanField,
)

from rss.models import Feed
from rss.widgets.date import DateInput


class FeedForm(ModelForm):
    template_name = "feed/form.html"
    enabled = BooleanField(
        required=False,
        initial=True,
        label="Enabled",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (
            self.instance
            and self.instance.pk
            and hasattr(self.instance, "periodic_task")
        ):
            self.initial["enabled"] = self.instance.enabled

    def save(self, commit: bool = True):
        feed = super().save(False)
        enabled = self.cleaned_data.get("enabled", False)
        if hasattr(feed, "periodic_task") and feed.periodic_task:
            feed.periodic_task.enabled = enabled
            if commit:
                feed.periodic_task.save()
        if commit:
            feed.save()
        return feed

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
            "torrent_clients",
        )
        labels = {
            "start_paused": "Start paused",
            "chronological": "Chronological",
            "torrent_clients": "Clients",
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "url": TextInput(attrs={"class": "form-control"}),
            "regex_filter": TextInput(attrs={"class": "form-control"}),
            "expires_at": DateInput(attrs={"class": "form-control"}),
            "download_dir": TextInput(attrs={"class": "form-control"}),
            "ignore_older_than": DateInput(attrs={"class": "form-control"}),
            "ignore_newer_than": DateInput(attrs={"class": "form-control"}),
            "start_paused": CheckboxInput(attrs={"class": "form-check-input"}),
            "chronological": CheckboxInput(attrs={"class": "form-check-input"}),
            "torrent_clients": SelectMultiple(attrs={"class": "form-select"}),
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
            "torrent_clients": None,
        }
