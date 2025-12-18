from django.forms import TextInput, ModelForm

from rss.models import Torrent
from rss.widgets.date import DateTimeInput


class TorrentForm(ModelForm):
    template_name = "client/form.html"

    class Meta:
        model = Torrent
        fields = (
            "title",
            "link",
            "published",
        )
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "link": TextInput(attrs={"class": "form-control"}),
            "published": DateTimeInput(attrs={"class": "form-control"}),
        }
