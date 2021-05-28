import discord
from discord.ext import commands 
import os  #to bring in the key

my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix = '?')
client.remove_command('help')



"""Ping/Pong"""
@client.event
async def on_ready():
    print('Logged on as', client.user)
@client.event
async def on_message(message):
    # don't respond to ourselves
    
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong!')
    await client.process_commands(message)

""" Commands"""

#kicks out a member
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user:discord.Member, *, reason = None):
    await user.kick(reason=reason)


#bans a member
@client.command(name="ban", help="command to ban user")
@commands.has_permissions(ban_members=True)
async def _ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send(f'{member.name} has been banned from server'
                               f'Reason: {reason}')
    except Exception:
        await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")

#look into why the code isn't passing the id, id isn't being calculated 
#unbans members
@client.command(name="unban", help="command to unban user")
@commands.has_permissions(administrator=True)
async def _unban(ctx, *, id):
    """ command to unban user. check !help unban """
    
    await ctx.guild.unban(discord.Object(id=id))
    await ctx.send(f"Unban {id}")

#repeats the past message
@client.command()
async def repeat(ctx, arg):
  await ctx.send(arg)

#clears past 3 messages
@client.command()
async def clear(ctx, amount=3):
  await ctx.channel.purge(limit=amount+1)        


#begin to add commands & examples from github rep.


# #clearing the past 3,5 or 10 messages





#add more deets for permissions on who can ban people

client.run(my_secret)
my_secret = os.environ['TOKEN']
print (my_secret)