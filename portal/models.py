from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    
    class Status(models.TextChoices):
        status_open = 'open', _('Open')
        status_in_progress = 'in_progress', _('In Progress')
        status_resolved = 'resolved', _('Resolved')
        status_closed = 'closed', _('Closed')
        
    class Priority(models.TextChoices):
        priority_urgent = 'urgent', _('Urgent')
        priority_high = 'high', _('High')
        priority_medium = 'medium', _('Medium')
        priority_low = 'low', _('Low')
    
    user = models.ForeignKey(User, related_name='user', blank=True, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(User, related_name='agent', blank=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(choices=Status.choices, max_length=11)
    priority = models.CharField(choices=Status.choices, max_length=11)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Ticket_History(models.Model):
    
    class Action(models.TextChoices):
        action_created = 'created', _('Created')
        action_updated = 'updated', _('Updated')
        action_assigned = 'assigned', _('Assigned')
        action_reassigned = 'reassigned', _('Re-assigned')
        action_resolved = 'resolved', _('Resolved')
        action_closed = 'closed', _('Closed')
        action_reopened = 'reopened', _('Re-opened')
    
    ticket = models.ForeignKey(Ticket, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    action = models.CharField(choices=Action.choices, max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return str(self.ticket.title)