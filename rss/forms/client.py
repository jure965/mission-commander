from django.contrib.auth.forms import UsernameField
from django.forms import ModelForm, CharField, PasswordInput, TextInput

from rss.models import TransmissionClient


class TransmissionClientForm(ModelForm):
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
        model = TransmissionClient
        fields = (
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
            "name": TextInput(attrs={"class": "form-control"}),
            "protocol": TextInput(attrs={"class": "form-control"}),
            "host": TextInput(attrs={"class": "form-control"}),
            "port": TextInput(attrs={"class": "form-control"}),
            "rpc_path": TextInput(attrs={"class": "form-control"}),
        }
