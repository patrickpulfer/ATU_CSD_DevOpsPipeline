from django.test import TestCase
from django.contrib.auth.models import User
from portal.models import Ticket, Ticket_History
from portal.forms import Ticket_History_Form


class TicketHistoryForm_TestCase(TestCase):

    def setUp(self):
        random_password = User.objects.make_random_password()
        self.user = User.objects.create_user(username='testuser', password=random_password)
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            description='This is a test ticket.',
            priority='low',
            status='open',
            user=self.user,
            agent=self.user,
        )

        self.ticket_history = Ticket_History.objects.create(
            action='updated',
            comment='some comment',
            ticket = self.ticket,
            user = self.user,
        )

    def test_ticket_history_form_valid(self):
        form_data = {
            'action': self.ticket_history.action,
            'comment': self.ticket_history.comment,
        }
        form = Ticket_History_Form(data=form_data)

        self.assertTrue(form.is_valid())

    def test_ticket_history_form_invalid(self):
        form_data = {
            'action': 'invalid action',
            'comment': self.ticket_history.comment,
        }
        form = Ticket_History_Form(data=form_data)

        self.assertFalse(form.is_valid())