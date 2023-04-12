#importing modules
#sdfs
import discord
import random
import json
from discord import user
from discord import channel
from discord.ext import commands
from discord import voice_client
from discord.ext.commands.core import guild_only
#making bot (intent are the previlage esclation for the bot so that it can access the member lisst or the the gluid)
# intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
# defing bot
client = commands.Bot(command_prefix = get_prefix)
# assigning the prefix according to server.
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Life is Chilled Out'))
    print("Bot's up and running")
@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = '. '
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes, f, indent=4)
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open('prefixes.json','w') as f:
            json.dump(prefixes,f,indent=4)
@client.command()
async def change_prefix(ctx, prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open('prefixes.json','w') as f:
            json.dump(prefixes, f, indent = 4)
            await ctx.send(f'prefix changed to {prefix}') 
#assigning tasks
@client.command()
async def ping(ctx):
    await ctx.send(f'pong!{round(client.latency*1000)}ms')
@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    
@client.event
async def on_member_remove(member):
    print(f'{member} has been removed')
@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def ban(ctx,member:discord.member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def unban(ctx,*,member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator)==(member_name,-member.discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned{user.mention}')
            return
@client.command(aliases = ['8ball,test'])
async def _8ball(ctx, *, question):
    responces = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question:{question}\n Answer: {random.choice(responces)}')
@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('no one in the voice chat!')
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client): # checks if bot is in vc
        await ctx.send("i left the voice channel as you said")
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("i haven't joined")


# calling bot
client.run('ODU4NjA0NDk3NzY4MDIyMDI2.YNgjwA.hnCHalRaE4vJuStMOzkR58Z5YjI')
@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client.voice):
        channel = ctx.guild.channel.VoiceChannel.channel
        await voice_client.disconnect()
    if (ctx.voice_client): # we don't have to use if(ctx.guild.voice_client):
        await ctx.voice_client.channel.disconnect()
        await ctx.send("i left the voice channel as you said")
    else:
        await ctx.send("i haven't joined")
# calling bot
client.run('ODU4NjA0NDk3NzY4MDIyMDI2.YNgjwA.ir62cwQsbo10p0pkHGMoK4OLWz8')
