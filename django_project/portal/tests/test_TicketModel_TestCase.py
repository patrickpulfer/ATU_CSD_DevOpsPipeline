from django.test import TestCase
from django.contrib.auth.models import User
from portal.models import Ticket


class TicketModel_TestCase(TestCase):

    def setUp(self):
        random_password = User.objects.make_random_password()
        self.user = User.objects.create_user(username='testuser', password=random_password)
        self.agent = User.objects.create_user(username='testagent', password=random_password)
        self.ticket = Ticket.objects.create(
            user=self.user,
            agent=self.agent,
            title='Test Ticket',
            description='Test Ticket Description',
            status=Ticket.Status.status_open,
            priority=Ticket.Priority.priority_medium,
        )

    def test_ticket_creation(self):
        ticket = Ticket.objects.get(pk=self.ticket.pk)
        self.assertEqual(ticket.title, 'Test Ticket')
        self.assertEqual(ticket.description, 'Test Ticket Description')
        self.assertEqual(ticket.status, 'open')
        self.assertEqual(ticket.priority, 'medium')
        self.assertEqual(ticket.user, self.user)
        self.assertEqual(ticket.agent, self.agent)

    def test_ticket_str_representation(self):
        self.assertEqual(str(self.ticket), 'Test Ticket')