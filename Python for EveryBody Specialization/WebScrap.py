import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum1 = 0
url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
    sum1 = sum1 + int(tag.contents[0])
print(sum1)
