import discord
from discord.ext import commands
import os
import pickle

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

client.remove_command('help')

for filename in os.listdir('./Commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')


with open('Token.pkl', 'rb') as file:
    Token = pickle.load(file)
    client.run(Token)
