#bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break

	print(f'{client.user} has connected to DISCORD!')
	print(f'on server {guild.name} ; \n id: {guild.id}')
	
	members = '\n - '.join([members.name for members in guild.members])
	print(f'Guild Members : \n - {members}')
client.run(TOKEN)
