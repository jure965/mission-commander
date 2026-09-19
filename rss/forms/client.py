from django.contrib.auth.forms import UsernameField
from django.forms import ModelForm, CharField, PasswordInput, TextInput, Select

from rss.models import TorrentClient


class TorrentClientForm(ModelForm):
    template_name = "client/form.html"

    username = UsernameField(
        required=False,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    password = CharField(
        label="Password",
        strip=False,
        required=False,
        widget=PasswordInput(render_value=True, attrs={"class": "form-control"}),
    )

    class Meta:
        model = TorrentClient
        fields = (
            "client_type",
            "name",
            "protocol",
            "host",
            "port",
            "username",
            "password",
            "rpc_path",
        )
        labels = {
            "rpc_path": "RPC path",
        }
        widgets = {
            "client_type": Select(attrs={"class": "form-control"}),
            "name": TextInput(attrs={"class": "form-control"}),
            "protocol": Select(attrs={"class": "form-control"}),
            "host": TextInput(attrs={"class": "form-control"}),
            "port": TextInput(attrs={"class": "form-control"}),
            "rpc_path": TextInput(attrs={"class": "form-control"}),
        }
