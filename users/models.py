from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('undefined', 'undefined')
    )

    gender = models.CharField(choices=GENDER_CHOICES, default='undefined', max_length=9)
    city = models.CharField(blank=True, default='', max_length=100)
    phone = models.CharField(blank=True, default='', max_length=12)
    email = models.EmailField(_('email'), unique=True, )
