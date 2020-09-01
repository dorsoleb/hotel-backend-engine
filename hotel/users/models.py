from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from users.fields import PhoneField
# Create your models here.


class Organization(models.Model):
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[AbstractUser.username_validator],
        error_messages={'unique': 'Пользователь с таким логином уже существует.'},
    )

    first_name = models.CharField(max_length=150,)

    last_name = models.CharField(max_length=150,)
    email = models.EmailField(unique=True, error_messages={'unique': 'Пользователь с таким email уже существует.'})
    mobile_phone = PhoneField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    date_leaved = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.DO_NOTHING,
        related_name='users',
    )
