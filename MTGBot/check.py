import re
import json

# Opening JSON file
f = open('MTGBot\default-cards-20211220100241.json', encoding='cp850')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# initialise the card dictionary
cardDictionary = {}

# Iterating through the json
# list
for i in data["cards"]:
    print(i['name'])
    if i['legalities']['commander'] == 'legal':
        if "//" in i['name']:
            if ('Creature' in i['type_line']) or ('Land' in i['type_line']):
                if ('Sorcery' not in i['type_line']) and ('Instant' not in i['type_line']):
                    cardDictionary[i['name']] = [i['card_faces'][0]['image_uris']['large'], i['card_faces'][1]['image_uris']['large']]
                else:
                    cardDictionary[i['name']] = [i['image_uris']['large']]

            elif any(word in 'Instant Sorcery' for word in i['type_line']):
                cardDictionary[i['name']] = [i['image_uris']['large']]
        else:
            cardDictionary[i['name']] = [i['image_uris']['large']]
    
print(cardDictionary[1]) 
# Closing file
f.close()