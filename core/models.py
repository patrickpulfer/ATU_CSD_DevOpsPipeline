from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    
    class Role(models.TextChoices):
        USER = 'User', _('User')
        AGENT = 'Agent', _('Support Agent')
        ADMIN = 'Admin', _('Administrator')
        

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(
        choices=Role.choices,
        max_length=5,
        )