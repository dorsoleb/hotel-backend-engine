from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r'^\d{11}$',
)


class PhoneField(models.CharField):
    description = "phone"
    default_validators = [phone_validator]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super().__init__(*args, **kwargs)
