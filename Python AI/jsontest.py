import json
from os import path
 
filename = 'Python AI/users.json'
listObj = []
print(listObj)
# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)

 

 





