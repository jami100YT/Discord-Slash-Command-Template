from dotenv import load_dotenv
import os
import discord

load_dotenv()
TOKEN = os.getenv("TOKEN")

# setting up the bot
intents = discord.Intents.all() 
# if you don't want all intents you can do discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# sync the slash command to your server
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=Your Guild Id))
    # print "ready" in the console when the bot is ready to work
    print("ready")

# make the slash command
@tree.command(name="hello", description="description", guild=discord.Object(id=Your Guild Id))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("Hello World")

# run the bot
client.run(TOKEN)
