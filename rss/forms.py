from django.contrib.auth.forms import UsernameField
from django.forms import ModelForm, CharField, PasswordInput

from rss.models import TransmissionClient


class TransmissionClientForm(ModelForm):
    username = UsernameField()
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(render_value=True),
        required=False,
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
