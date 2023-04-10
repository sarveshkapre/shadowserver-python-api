# shadowserver-python-api
A lightweight Python library for accessing the Shadowserver API, allowing users to easily query and download reports related to security events and network activity.

## Installation
To install the Shadowserver API client, simply run:

```
pip install -r requirements.txt
```

## Usage
To use the Shadowserver API client, you will need to first create an authentication object by providing your API key and secret. This can be done by creating an instance of the ShadowserverAuth class:

```
from shadowserver.auth import ShadowserverAuth


SHADOWSERVER_API_KEY="SHADOWSERVER_API_KEY"
SHADOWSERVER_SECRET="SHADOWSERVER_SECRET"

auth = ShadowserverAuth('SHADOWSERVER_API_KEY', 'SHADOWSERVER_SECRET')
```

Once you have an authentication object, you can create instances of the ShadowserverReportAPI, ShadowserverASNAPI, and ShadowserverSSLAPI classes to access the various API endpoints:

```
from shadowserver.report_api import ShadowserverReportAPI
from shadowserver.asn_api import ShadowserverASNAPI
from shadowserver.ssl_api import ShadowserverSSLAPI

SHADOWSERVER_URI="https://transform.shadowserver.org/api2/"

report_api = ShadowserverReportAPI(SHADOWSERVER_URI, auth)
asn_api = ShadowserverASNAPI(SHADOWSERVER_URI, auth)
ssl_api = ShadowserverSSLAPI(SHADOWSERVER_URI, auth)
```

You can then use the methods of these API classes to interact with the Shadowserver API endpoints. For example, to retrieve a list of available reports, you can use the list method of the ShadowserverReportAPI class:

```
reports = report_api.list()
print(reports)
```

For more information on the available methods for each API class, please refer to the corresponding Python files in the shadowserver package.

## Examples
For some examples on how to use the Shadowserver API client, please see the Jupyter notebooks provided in the examples directory.

## License
This code is licensed under the MIT License. Please see the LICENSE file for more information.

## Contributing
Pull requests and bug reports are welcome! Please see the CONTRIBUTING file for more information.

## Contact
If you have any questions or concerns about shadowserer APIs, please contact us at support@shadowserver.org.
