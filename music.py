#music functionality
import discord
from discord import voice_client
from discord import client
from discord import guild
from discord.ext import commands
import Code_discord
from Code_discord import *
from discord import user
from discord import channel



@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):    
        await ctx.guild.voice_client.disconnect()
        await ctx.send('I left the channel')
    else:
        await ctx.send('no')
