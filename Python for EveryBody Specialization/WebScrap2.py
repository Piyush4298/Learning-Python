import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
pos = int(input('Enter position: ')) - 1
url = input('Enter url: ')
count = int(input('Enter count: '))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for i in range(count):
    link = tags[pos].get('href', None)
    print('Retriving:', link)
    print(tags[pos].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
