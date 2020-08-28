import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">    
            <name>Piyush</name>
            <id>001</id>
        </user>
        <user x="7">
            <name>Dr.Chuck</name>
            <id>009</id>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('user count:',len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))
