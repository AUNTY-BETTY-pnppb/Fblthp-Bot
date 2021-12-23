import discord
import os
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

# initialize discord client
client = discord.Client()

# when bot is ready and setup
@client.event
async def on_ready():
    # set status online
    await client.change_presence(status=discord.Status.online)
    print("Holy shit, where are we?")

# when a message is sent
@client.event
async def on_message(message):
    # check first that message isn't from bot
    if message.author.name != "Fblthp-Bot":
        # find any instnace of [[*]] in message
        cards = re.findall("\[\[([^\[\]]*)\]\]", message.content)
        # print if there are cards read
        if len(cards) > 0 :
            for i in cards:
                await message.channel.send(i)
        
my_token = os.environ['Fblthp']
client.run(my_token)