from django import forms
from .models import *


class Ticket_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Ticket_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Ticket
        fields = {'title', 'description', 'priority'}

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'priority': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'})
    }


class Ticket_History_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Ticket_History_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Ticket_History
        fields = {'action', 'comment'}

    widgets = {
        'action': forms.Select(attrs={'class': 'form-control'}),
        'comment': forms.Textarea(attrs={'class': 'form-control'})
    }