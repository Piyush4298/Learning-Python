import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter url: ')
print('Retriving', url)
html = urllib.request.urlopen(url,context=ctx).read()
print('Retrived', len(html), 'characters')
tree = ET.fromstring(html)
results = tree.findall('comments/comment')

s = 0
c = 0
for i in results:
    c = c+1
    s = s + int(i.find('count').text)
print('Count:', c)
print('Sum:', s)
