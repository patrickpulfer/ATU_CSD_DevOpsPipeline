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


"""
    ticket = models.ForeignKey(Ticket, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)
    action = models.CharField(choices=Action.choices, max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

"""