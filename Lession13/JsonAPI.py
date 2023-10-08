import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

apiUrl = "http://py4e-data.dr-chuck.net/json?"

address = input('Enter location: ')
if len(address) < 1:
    address = "Czech Technical University in Prague"

parms = dict()
parms['address'] = address
parms['key'] = 42

url = apiUrl + urllib.parse.urlencode(parms)
print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx)

js = json.load(html)

# print(json.dumps(js, indent=4))

print("place_id:", js["results"][0]["place_id"])
