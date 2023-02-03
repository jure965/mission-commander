from django.forms import CheckboxInput as BuiltinCheckboxInput


class CheckboxInput(BuiltinCheckboxInput):
    template_name = "rss/widget/checkbox.html"

    def __init__(self, attrs=None, check_test=None, label=""):
        super().__init__(attrs, check_test)
        self.label = label

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["label"] = self.label
        return context
