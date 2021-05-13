import discord
from discord.ext import commands 
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
            await message.channel.send('pong!')

#begin to add commands & examples from github rep.
client = commands.Bot(command_prefix = '.')

#clearing the past 3,5 or 10 messages
@client.command()
async def clear(ctx, amount=3):
  await ctx.channel.purge(limit=amount)

#kicking a member of the discord group, make the person add a reason or ask permission before kicking someone
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

#add more deets for permissions on who can ban people
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)


client = MyClient()
client.run(my_secret)
my_secret = os.environ['TOKEN']
print (my_secret)