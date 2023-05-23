from django.test import TestCase
from django.contrib.auth.models import User
from portal.models import Ticket, Ticket_History


class TicketHistoryModel_TestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.ticket = Ticket.objects.create(
            user=self.user,
            title='Test Ticket',
            description='Test Ticket Description',
            status=Ticket.Status.status_open,
            priority=Ticket.Priority.priority_medium,
        )
        self.ticket_history = Ticket_History.objects.create(
            ticket=self.ticket,
            user=self.user,
            action=Ticket_History.Action.action_created,
            comment='Ticket created',
        )

    def test_ticket_history_creation(self):
        ticket_history = Ticket_History.objects.get(pk=self.ticket_history.pk)
        self.assertEqual(ticket_history.ticket, self.ticket)
        self.assertEqual(ticket_history.user, self.user)
        self.assertEqual(ticket_history.action, 'created')
        self.assertEqual(ticket_history.comment, 'Ticket created')

    def test_ticket_history_str_representation(self):
        self.assertEqual(str(self.ticket_history), 'Test Ticket')