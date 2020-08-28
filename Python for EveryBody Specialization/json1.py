import json

data= '''
{
    "name" : "Piyush",
    "phone" : {
        "type" : "intl",
        "number" : "+91 749 895 8716"
        },
    "email" : {
        "hide" : "Yes"
        }
    }'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])