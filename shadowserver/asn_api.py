import json
import requests


class ShadowserverASNAPI:
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

    def origin_query(self, origin):
        """
        Returns ASN details for the specified origin IP address.
        """
        api_request = {'origin': origin}
        return self._call_api('net/asn', api_request)

    def peer_query(self, peer):
        """
        Returns BGP peers for the specified IP address.
        """
        api_request = {'peer': peer}
        return self._call_api('net/asn', api_request)

    def prefix_query(self, asn, ipv6=False):
        """
        Returns the routed prefixes for the specified ASN.
        """
        api_request = {'prefix': asn}
        if ipv6:
            api_request['v6'] = True
        return self._call_api('net/asn', api_request)

    def asn_query(self, query):
        """
        Returns ASN details for the specified ASN number or name.
        """
        api_request = {'query': query}
        return self._call_api('net/asn', api_request)
