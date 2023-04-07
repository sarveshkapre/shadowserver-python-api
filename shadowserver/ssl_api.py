import json
import requests


class ShadowserverSSLAPI:
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

    def query(self, ip_address, port=None):
        """
        Queries SSL/TLS information for the specified IP address and port.
        """
        api_request = {'ip': ip_address}
        if port is not None:
            api_request['port'] = port
        return self._call_api('ssl/query', api_request)

    def history(self, ip_address, port=None):
        """
        Returns SSL/TLS certificate history for the specified IP address and port.
        """
        api_request = {'ip': ip_address}
        if port is not None:
            api_request['port'] = port
        return self._call_api('ssl/history', api_request)

    def lookup(self, certificate_hash):
        """
        Returns SSL/TLS certificate details for the specified SHA-1 hash.
        """
        api_request = {'hash': certificate_hash}
        return self._call_api('ssl/lookup', api_request)
