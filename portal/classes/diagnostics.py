from models import Diagnostics_Report
import requests


class Diagnostics:

    def __init__(self):
        self.WS1_Diagnostics_Module()


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
        service_id = 503
        service_domain = 'test.com'

        def __init__(self):
            self.getDiscovery()

        def getDiscovery(self):
            url = self.url_discovery + self.service_domain
            try:
                response = request.url(url)
                print(response)
            except:
                print("An exception occurred while querying discovery")





diagnostics = Diagnostics()



"""
url = 'https://www.example.com'
response = requests.get(url)

status_code = response.status_code
"""


"""

    ticket = models.ForeignKey(Ticket, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    enrollment_url = models.CharField(blank=True, null=True, max_length=200)
    enrollment_group = models.CharField(blank=True, null=True, max_length=50)
    awcm_status = models.BooleanField(default=False)
    awcm_link = models.URLField(blank=True, null=True, max_length=200)
    cn_status = models.BooleanField(default=False)
    ds_status = models.BooleanField(default=False)
    app_catalog = models.BooleanField(default=False)
    service_status_indicator = models.CharField(blank=True, null=True, max_length=200)
    service_status_description = models.CharField(blank=True, null=True, max_length=200)

Diagnostics
CheckboxInput

https://discovery.awmdm.com/Autodiscovery/awcredentials.aws/v2/domainlookup/domain/test.com
{"EnrollmentUrl":"https://sdalmieda-W01.vmware.com/DeviceManagement/Enrollment","GroupId":"Test"}

https://cn135.awmdm.com/AirWatch/
https://awcm135.awmdm.com/awcm/status/
https://awcm135.awmdm.com/awcm/statistics/

Device Management, 1 value
Web Console, 1 value
AWCM
"""