from django.forms.fields import CharField
from regex_field.fields import RegexField as BrokenRegexField


class RegexFormField(CharField):
    def prepare_value(self, value):
        try:
            return value.pattern
        except AttributeError:
            return value


class RegexField(BrokenRegexField):
    def formfield(self, **kwargs):
        defaults = {"form_class": RegexFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
