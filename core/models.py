from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    
    class Role(models.TextChoices):
        user_role = 'user', _('User')
        agent_role = 'agent', _('Support Agent')
        admin_role = 'admin', _('Administrator')


    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(choices=Role.choices, max_length=5)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()