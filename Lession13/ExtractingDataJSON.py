import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url:")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1904308.json"

html = urllib.request.urlopen(url, context=ctx)
content = json.load(html)

total = 0
for count in content["comments"]:
    total += int(count["count"])

print("Total count:", total)
