from django.forms import DateInput as BuiltinDateInput
from django.forms import DateTimeInput as BuiltinDateTimeInput


class DateInput(BuiltinDateInput):
    input_type = "date"


class DateTimeInput(BuiltinDateTimeInput):
    input_type = "datetime-local"
