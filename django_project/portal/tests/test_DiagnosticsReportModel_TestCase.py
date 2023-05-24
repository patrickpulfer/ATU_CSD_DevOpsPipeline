from django.test import TestCase
from django.contrib.auth.models import User
from portal.models import Ticket, Diagnostics_Report


class DiagnosticsReportModel_TestCase(TestCase):

    def setUp(self):
        random_password = User.objects.make_random_password()
        self.user = User.objects.create_user(username='testuser', password=random_password)
        self.ticket = Ticket.objects.create(
            user=self.user,
            title='Test Ticket',
            description='Test Ticket Description',
            status=Ticket.Status.status_open,
            priority=Ticket.Priority.priority_medium,
        )
        self.diagnostics_report = Diagnostics_Report.objects.create(
            ticket=self.ticket,
            enrollment_url='https://test-enrollment-url.com',
            enrollment_group='Test Group',
            awcm_status='Success',
            awcm_link='https://test-awcm-link.com',
            cn_status=True,
            ds_status=False,
            app_catalog=True,
            service_status_indicator='All services are working',
            service_status_description='All services are working as expected',
        )

    def test_diagnostics_report_creation(self):
        diagnostics_report = Diagnostics_Report.objects.get(pk=self.diagnostics_report.pk)
        self.assertEqual(diagnostics_report.ticket, self.ticket)
        self.assertEqual(diagnostics_report.enrollment_url, 'https://test-enrollment-url.com')
        self.assertEqual(diagnostics_report.enrollment_group, 'Test Group')
        self.assertEqual(diagnostics_report.awcm_status, 'Success')
        self.assertEqual(diagnostics_report.awcm_link, 'https://test-awcm-link.com')
        self.assertTrue(diagnostics_report.cn_status)
        self.assertFalse(diagnostics_report.ds_status)
        self.assertTrue(diagnostics_report.app_catalog)