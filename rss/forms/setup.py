from django import forms
from django.contrib.auth.forms import UsernameField
from django.forms import Form
from django.utils.translation import gettext_lazy as _


class SetupForm(Form):
    template_name = "setup/form.html"
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )
