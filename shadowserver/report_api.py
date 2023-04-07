import json
import requests


class ShadowserverReportAPI:
    TIMEOUT = 45

    def __init__(self, uri, auth):
        self.uri = uri
        self.auth = auth

    def _call_api(self, method, request):
        url = self.uri + method
        headers = self.auth.get_headers(request)
        response = requests.post(url, data=json.dumps(request), headers=headers, timeout=self.TIMEOUT)
        response.raise_for_status()
        return response.json()

    def types(self, detail=False):
        """
        Returns a list of report types with optional detailed information.
        """
        api_request = {}
        if detail:
            api_request['detail'] = True
        return self._call_api('reports/types', api_request)

    def subscribed(self):
        """
        Returns a list of subscribed reports for the authenticated user.
        """
        return self._call_api('reports/subscribed', {})

    def list(self, limit=None, latest=False):
        """
        Returns a list of available reports for the authenticated user, limited by the specified number or the latest report.
        """
        api_request = {}
        if latest:
            api_request['limit'] = 1
        elif limit is not None:
            api_request['limit'] = limit
        return self._call_api('reports/list', api_request)

    def download(self, report_id):
        """
        Downloads the report with the specified UUID.
        """
        api_request = {'id': report_id}
        return self._call_api('reports/download', api_request)

    def query(self, start_date, end_date, report_type=None, **kwargs):
        """
        Queries for reports based on the specified date range and optional filter criteria.
        """
        api_request = {'start_date': start_date, 'end_date': end_date}
        if report_type is not None:
            api_request['type'] = report_type
        api_request.update(kwargs)
        return self._call_api('reports/query', api_request)
    
    def device_info(self, ip_address):
        """
        Returns device details for the specified IP address.
        """
        api_request = {'ip': ip_address}
        return self._call_api('reports/device-info', api_request)

    def schema(self, report_type):
        """
        Returns the JSON schema for the specified report type.
        """
        api_request = {'type': report_type}
        return self._call_api('reports/schema', api_request)

    def stats(self, report_type, date_range=None):
        """
        Returns statistics for the specified report type.
        """
        api_request = {'type': report_type}
        if date_range is not None:
            api_request['date'] = date_range
        return self._call_api('reports/stats', api_request)
