from shadowserver.auth import ShadowserverAuth
from shadowserver.report_api import ShadowserverReportAPI
from shadowserver.asn_api import ShadowserverASNAPI
from shadowserver.ssl_api import ShadowserverSSLAPI

auth = ShadowserverAuth('YOUR_API_KEY', 'YOUR_SECRET_KEY')
report_api = ShadowserverReportAPI('https://api.shadowserver.org/', auth)
asn_api = ShadowserverASNAPI('https://api.shadowserver.org/', auth)
ssl_api = ShadowserverSSLAPI('https://api.shadowserver.org/', auth)

# Example report API usage
types = report_api.types()
print(f"Report types: {types}")

subscribed = report_api.subscribed()
print(f"Subscribed reports: {subscribed}")

reports = report_api.list(latest=True)
print(f"Latest report: {reports}")

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
