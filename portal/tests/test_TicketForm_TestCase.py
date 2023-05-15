from django.test import TestCase
from portal.forms import Ticket_Form


class TicketForm_TestCase(TestCase):

    def test_ticket_form_valid(self):
        form = Ticket_Form(data={
            'title': 'Test Ticket',
            'description': 'This is a test ticket.',
            'priority': 'low',
            'status': 'open'
        })

        self.assertTrue(form.is_valid())

    def test_ticket_form_invalid(self):
        form = Ticket_Form(data={
            'title': '',
            'description': 'This is a test ticket.',
            'priority': 'low',
            'status': 'open'
        })
        self.assertFalse(form.is_valid())