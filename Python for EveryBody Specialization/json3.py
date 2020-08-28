import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url: ')
print('Retrieving', url)
html = urllib.request.urlopen(url).read()
html.decode()
print('Retrieved', len(html), 'characters')
info = json.loads(html)
results = info.get('comments')
print('Count:',len(results))
s = 0
for i in results:
    s = s + int(i["count"])
print('Sum:',s)