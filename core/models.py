from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()