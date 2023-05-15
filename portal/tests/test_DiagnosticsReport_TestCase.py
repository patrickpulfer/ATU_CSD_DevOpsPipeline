from django.test import TestCase, Client
from portal.classes.diagnostics import WS1_Diagnostics_Module


class Diagnostics_Discovery_TestCase(TestCase):
    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()        
        self.client = Client()
        self.result = self.diagnostics_to_load.getDevicesStatus()

    def test_positive_Discovery(self):
        self.assertEqual(self.result, True)

    def test_negative_Discovery(self):         
        self.assertNotEqual(self.result, False)


class Diagnostics_ConsoleStatus_TestCase(TestCase):

    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()
        self.client = Client()
        self.result = self.diagnostics_to_load.getConsoleStatus()

    def test_positive_ConsoleStatus(self):
        self.assertEqual(self.result, True)

    def test_negative_ConsoleStatus(self):
        self.assertNotEqual(self.result, False)


class Diagnostics_DeviceStatus_TestCase(TestCase):

    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()
        self.client = Client()
        self.result = self.diagnostics_to_load.getDevicesStatus()

    def test_positive_DeviceStatus(self):
        self.assertEqual(self.result, True)

    def test_negative_DeviceStatus(self):
        self.assertNotEqual(self.result, False)


class Diagnostics_AppCatalog_TestCase(TestCase):

    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()
        self.client = Client()
        self.result = self.diagnostics_to_load.getApp_Catalog_Status()

    def test_positive_AppCatalog(self):
        self.assertEqual(self.result, True)

    def test_negative_AppCatalog(self):
        self.assertNotEqual(self.result, False)


class Diagnostics_AWCMStatus_TestCase(TestCase):

    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()
        self.client = Client()
        self.result = self.diagnostics_to_load.getAWCM_status()

    def test_positive_AWCMStatus(self):
        self.assertEqual(self.result, 'OK')

    def test_negative_AWCMStatus(self):
        self.assertNotEqual(self.result, False)


class Diagnostics_ServiceStatus_TestCase(TestCase):

    def setUp(self):
        self.diagnostics_to_load = WS1_Diagnostics_Module()
        self.client = Client()
        self.result = self.diagnostics_to_load.getServiceStatus()

    def test_positive_ServiceStatus(self):
        print(self.result)
        self.assertContains(self.result, 'status')

    def test_negative_ServiceStatus(self):
        self.assertNotEqual(self.result, False)