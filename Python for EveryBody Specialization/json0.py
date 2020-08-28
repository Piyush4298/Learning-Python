import json

inp = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    } ,
    { "id" : "006",
      "x" : "7",
      "name" : "Pandu" 
    }
]'''

info = json.loads(inp)
print('User count:',len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])