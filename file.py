def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix, intents = intents)
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
