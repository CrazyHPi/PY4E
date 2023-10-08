from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Meriem.html"

for i in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup("a")

    url = tags[17].get("href")
    print("goto:", url)