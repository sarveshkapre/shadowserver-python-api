import json
import hmac
import hashlib


class ShadowserverAuth:
    """Class for handling authentication to the Shadowserver API."""

    def __init__(self, key, secret):
        """Constructor method to initialize the ShadowserverAuth object.

        Args:
            key (str): API key for the Shadowserver API.
            secret (str): Secret key for the Shadowserver API.
        """
        self.key = key
        self.secret = secret

    def _generate_hmac(self, message):
        """Method to generate HMAC digest for authentication.

        Args:
            message (str): Request message to generate HMAC digest for.

        Returns:
            str: HMAC digest.
        """
        secret_bytes = bytes(str(self.secret), 'utf-8')
        message_bytes = bytes(message, 'utf-8')
        hmac_generator = hmac.new(secret_bytes, message_bytes, hashlib.sha256)
        return hmac_generator.hexdigest()

    def get_headers(self, request):
        """Method to get headers for API requests.

        Args:
            request (dict): Request dictionary to get headers for.

        Returns:
            dict: Dictionary containing headers for the API request.
        """
        request['apikey'] = self.key
        request_string = json.dumps(request)
        hmac_digest = self._generate_hmac(request_string)
        return {'HMAC2': hmac_digest}
