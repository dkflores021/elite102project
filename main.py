import discord
import os  #to bring in the key
my_secret = os.environ['TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

#begin to add commands & examples from github rep. 



client = MyClient()
client.run(my_secret)
my_secret = os.environ['TOKEN']
print (my_secret)