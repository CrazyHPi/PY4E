import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url:")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1904307.xml"

html = urllib.request.urlopen(url, context=ctx).read()
xmlTree = ET.fromstring(html.decode())
# print(xmlTree)
# print(xmlTree.findall('.//count')) same as the following line
commentList = xmlTree.findall("comments")[0].findall("comment")

total = 0

for item in commentList:
    total += int(item.findall("count")[0].text)

print("Total count:", total)
