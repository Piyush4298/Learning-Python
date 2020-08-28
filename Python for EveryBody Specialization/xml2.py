import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Piyush</name>
    <phone type="intl">
        +91 9130599634
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))