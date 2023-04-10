from shadowserver.auth import ShadowserverAuth
from shadowserver.report_api import ShadowserverReportAPI
from shadowserver.asn_api import ShadowserverASNAPI
from shadowserver.ssl_api import ShadowserverSSLAPI

SHADOWSERVER_API_KEY="SHADOWSERVER_API_KEY"
SHADOWSERVER_SECRET="SHADOWSERVER_SECRET"
SHADOWSERVER_URI="https://transform.shadowserver.org/api2/"

auth = ShadowserverAuth('SHADOWSERVER_API_KEY', 'SHADOWSERVER_SECRET')
report_api = ShadowserverReportAPI(SHADOWSERVER_URI, auth)
asn_api = ShadowserverASNAPI(SHADOWSERVER_URI, auth)
ssl_api = ShadowserverSSLAPI(SHADOWSERVER_URI, auth)

# Example report API usage
types = report_api.types()
print(f"Report types: {types}")

subscribed = report_api.subscribed()
print(f"Subscribed reports: {subscribed}")

reports = report_api.list(latest=True)
print(f"Latest report: {reports}")

# Get the last 5 reports
report_api.list(limit=5)

# Get the ID of the most recent report
report_info = reports[0] if reports else {}
report_id = report_info.get('id')
print(report_id)

# Get a list of available reports for the authenticated user
reports_list = report_api.list()

# Loop through the list and download each report
for report_info in reports_list:
    print(report_info.get('type'))
    report_id = report_info.get('id')
    print(report_id)
    response = api.reports_download(report_id)
    print(response)
    # do something with the downloaded report, such as write it to a file
    # e.g. with open(report_id + '.json', 'w') as f:
    #          f.write(json.dumps(response))

report_id = "REPORT_UUID"
report_data = report_api.download(report_id)
print(f"Downloaded report data: {report_data}")

# Example ASN API usage
origin_details = asn_api.origin_query("8.8.8.8")
print(f"Origin details for 8.8.8.8: {origin_details}")

peer_details = asn_api.peer_query("8.8.8.8")
print(f"BGP peers for 8.8.8.8: {peer_details}")

prefixes = asn_api.prefix_query("AS15169")
print(f"Routed prefixes for AS15169: {prefixes}")

asn_details = asn_api.asn_query("AS15169")
print(f"Details for AS15169: {asn_details}")

# Example SSL API usage
ssl_details = ssl_api.query("google.com")
print(f"SSL details for google.com: {ssl_details}")
