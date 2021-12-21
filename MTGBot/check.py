import re
import json

# Opening JSON file
f = open('MTGBot\default-cards-20211220100241.json', encoding='cp850')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data["cards"]:
    print(i)
 
# Closing file
f.close()