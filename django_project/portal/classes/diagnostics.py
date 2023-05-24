import requests, json
from dataclasses import dataclass


class Diagnostics:
    loaded_modules: str
    def __init__(self):
        self.loaded_modules = "WS1_Diagnostics_Module"


class WS1_Diagnostics_Module:

    # Default URLs for WS1 diagnostics module
    url_discovery = 'https://discovery.awmdm.com/Autodiscovery/awcredentials.aws/v2/domainlookup/domain/'
    url_console = 'https://cnVALUE.awmdm.com/AirWatch/'
    url_devices = 'https://dsVALUE.awmdm.com/AirWatch/DeviceManagement/enrollment'
    url_app_catalog = 'https://dsVALUE.awmdm.com/AirWatch/DeviceManagement/appcatalog?uid=0'
    url_awcm = 'https://awcmVALUE.awmdm.com/awcm/status/'
    url_awcm_statistics = 'https://awcmVALUE.awmdm.com/awcm/statistics/'
    url_service_status = 'https://status.workspaceone.com/api/v2/status.json'
    url_service_history = 'https://status.workspaceone.com/history.rss'

    # Default environmental information
    service_id = 135
    service_domain = 'test.com'

    # Initial variables
    discover : str
    console_status: bool
    devices_status: bool
    app_catalog_status: bool
    awcm_status: str
    service_status: json

    def __init__(self):
        self.discover = self.getDiscovery()
        self.console_status = self.getConsoleStatus()
        self.devices_status = self.getDevicesStatus()
        self.app_catalog_status = self.getApp_Catalog_Status()
        self.awcm_status = self.getAWCM_status()
        self.service_status = self.getServiceStatus()

    def getDiscovery(self):
        url = self.url_discovery + self.service_domain
        try:
            response = requests.get(url, timeout=5).json()
        except:
            print("An exception occurred while querying discovery")
        return response

    def getConsoleStatus(self):
        status_code = bool
        url = self.url_console.replace('VALUE', str(self.service_id))
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
        except:
            print("An exception occurred while querying console status")
        if status_code == 200:
            result = True
        else:
            result = False
        return result
    
    def getDevicesStatus(self):
        status_code = bool
        url = self.url_devices.replace('VALUE', str(self.service_id))
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
        except:
            print("An exception occurred while querying devices status")
        if status_code == 200:
            result = True
        else:
            result = False
        return result

    def getApp_Catalog_Status(self):
        status_code = bool
        url = self.url_app_catalog.replace('VALUE', str(self.service_id))
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
        except:
            print("An exception occurred while querying app catalog status")
        if status_code == 200:
            result = True
        else:
            result = False
        return result

    def getAWCM_status(self):
        url = self.url_awcm.replace('VALUE', str(self.service_id))
        try:
            response = requests.get(url, timeout=5)
        except:
            print("An exception occurred while querying app catalog status")
        return response.text

    def getServiceStatus(self):
        url = self.url_service_status
        try:
            response = requests.get(url, timeout=5).json()
        except:
            print("An exception occurred while querying discovery")
        return response


diagnostics_to_load = Diagnostics()