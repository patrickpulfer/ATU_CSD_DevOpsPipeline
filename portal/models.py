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
    agent = models.ForeignKey(User, related_name='agent', blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(choices=Status.choices, max_length=11)
    priority = models.CharField(choices=Priority.choices, max_length=11)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
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
    
    ticket = models.ForeignKey(Ticket, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)
    action = models.CharField(choices=Action.choices, max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return str(self.ticket.title)
    

class Diagnostics_Report(models.Model):

    ticket = models.ForeignKey(Ticket, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    enrollment_url = models.CharField(blank=True, null=True, max_length=200)
    enrollment_group = models.CharField(blank=True, null=True, max_length=50)
    awcm_status = models.CharField(max_length=50)
    awcm_link = models.URLField(blank=True, null=True, max_length=200)
    cn_status = models.BooleanField(default=False)
    ds_status = models.BooleanField(default=False)
    app_catalog = models.BooleanField(default=False)
    service_status_indicator = models.CharField(blank=True, null=True, max_length=200)
    service_status_description = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return str(self.ticket.title)