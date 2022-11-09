import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

with open(sampleJson) as sampleJson:
    json_decoded = json.load(sampleJson)

json_decoded['ADDED_KEY'] = 'ADDED_VALUE'

with open(sampleJson, 'w') as sampleJson:
    json.dump(json_decoded, sampleJson)


sampleJson = "my_file.json"

with open(sampleJson, 'w') as file_obj:
    json.dump(sampleJson, file_obj)
   
