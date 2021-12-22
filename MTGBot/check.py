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
            cardDictionary[i['name']] = {'image' : [i['image_uris']['large']], 'euro' : i['prices']['eur']}
        # else for the double-faced
        else:
            cardDictionary[i['name']] = {'image' : [i['card_faces'][0]['image_uris']['large'],
                                         i['card_faces'][1]['image_uris']['large']], 'euro' : i['prices']['eur']}

# Closing file
f.close()

# search engine for cards
def search():
    # take input
    print('Read to take input: ')
    userInput = input()

    # make sure it is valid length
    if len(userInput) > 2:
        # sift through the dictionary
        for card in cardDictionary.keys():
            # compare the card with the input
            if any(word in userInput.lower().split() for word in card.lower().split()):
                print(card, end=" ")
                print(cardDictionary[card])
    # else print as invalid
    else:
        print('Invalid input length of ' + str(len(userInput)) + ' characters')

search()