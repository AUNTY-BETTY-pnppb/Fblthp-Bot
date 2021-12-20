import discord
import os
import re
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Holy shit, where are we?")

@client.event
async def on_message(message):
    if message.author.name != "Fblthp-Bot":
        cards = re.findall("\[\[([^\[\]]*)\]\]", message.content)
        if len(cards) > 0 :
            for i in cards:
                await message.channel.send(i)
        
my_token = os.environ['Fblthp']
client.run(my_token)
