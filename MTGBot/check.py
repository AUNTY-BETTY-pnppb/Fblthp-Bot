import json

# Opening JSON file
f = open('MTGBot\default-cards-20211220100241.json', encoding='cp850')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# initialise the card dictionary
cardDictionary = {}

# Iterating through the json
for i in data["cards"]:
    # If the card is commander legal
    if i['legalities']['commander'] == 'legal':
        # check if the image is not double-faced
        if 'image_uris' in i.keys():
            cardDictionary[i['name']] = {'image' : [i['image_uris']['large']]}
        # else for the double-faced
        else:
            cardDictionary[i['name']] = {'image' : [i['card_faces'][0]['image_uris']['large'],
                                         i['card_faces'][1]['image_uris']['large']]}

# Closing file
f.close()

faves = ['Colossal Dreadmaw', 'Gishath', 'Ghave', 'Tayam', 'Chatterfang']

# search engine for cards
def search(input):
    extras = {}
    input = input.replace(",", "")
    # make sure it is valid length
    if len(input) > 1:
        # sift through the dictionary
        for card in cardDictionary.keys():
            # remove the ',' in card titles
            cardCheck = card.replace(",", "")
            if input in cardDictionary.keys():
                print(input, end=' ')
                print(cardDictionary[input])
                return
            if any(word in input.lower().split() for word in cardCheck.lower().split()):
                if card not in extras.keys():
                    extras[card] = cardDictionary[card]  
        # if no single found then print the list
        for card in extras.keys():
            if len(extras) == 1:
                print(card, end=' ')
                print(extras[card])
                return
            print(card)

    # else print as invalid
    else:
        print('Invalid input length of ' + str(len(input)) + ' characters')

search('Dreadmaw')