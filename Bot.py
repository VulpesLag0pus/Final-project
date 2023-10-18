import discord
import json
from discord.ext import commands
import requests

#Getting meme from reddit:
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

#Logging in on bot account:
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0.user}!'.format(self))

    async def on_message(self, message):
       member = message.guild.get_member(#Replace with you user ID)
#Making sure bot issn't responding to itself:
       if message.author == self.user:
         return
       
#Checking if anyone dared to say my name:
       elif 'Vulpes' in message.content or member.mentioned_in(message):
#Getting my status:
           status = member.status
           print (status)
#Checking if I can respond:
           if status == discord.Status.online:
              await message.channel.send("Vulpes is online at the moment and will respond to you shortly, here's a meme while you wait.")
              await message.channel.send(get_meme())
           elif status == discord.Status.offline:
              await message.channel.send('Sorry, Vulpes is offline at the moment.')
              await message.channel.send(file=discord.File('Sleeping_Vulpes.gif'))
           elif status == discord.Status.dnd:
              await message.channel.send('Vulpes is probably sleeping, DO NOT DISTURB him!')
              await message.channel.send(file=discord.File('Sleeping_Vulpes.gif'))
           elif status == discord.Status.idle:
              await message.channel.send("Vulpes is barely awake, here's a meme while you wait for him to fully wake up.")
              await message.channel.send(get_meme())
           else:
              await message.channel.send("Vulpes? How is that? You looking for gosts or something?")
              


#Giving the bot premission to control my whole server(I know that is not what it does):
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
#Activating the bot
client = MyClient(intents=intents)
client.run('#Replace with your token')
