from django import forms
from .models import *


class Ticket_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Ticket_Form, self).__init__(*args, **kwargs)
        #self.fields['status'].initial = False


    class Meta:
        model = Ticket
        fields = {'title', 'description', 'priority'}

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'priority': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'})

    }