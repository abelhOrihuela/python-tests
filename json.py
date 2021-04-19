import simplejson as json
import os

newFile = open("ages.json", "w+")

# if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
#     old_file = open("./ages.json", "r+")
#     data = json.loads(old_file.read())

data = { "name": "Abel", "age": 27 }

newFile.write(json.dumps(data))
  
