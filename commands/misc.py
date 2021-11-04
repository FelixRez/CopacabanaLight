from discord.ext import commands
import math
import re
from random import random
from datetime import date

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.name = "Misc"
        self.today = date.today()
        self.randomValue = random()

    def RandomIndex(self, ArraySize):
        return math.floor(random() * ArraySize)

    @commands.command(name="ajuda",alisases=['h','help'],help="Misc:Lista de Comandos")
    async def ajuda(self,ctx):
        helptxt = 'Lista de Comandos\n'
        commandtxt = {}

        for command in self.client.commands:
            if command == "ajuda":
                continue

            cmdhelp = str(command.help).split(':')
            if cmdhelp[0] in commandtxt.keys():
                commandtxt[cmdhelp[0]] += f'!{command} --> {cmdhelp[1]}\n'
            else:
                commandtxt[cmdhelp[0]] = f'!{command} --> {cmdhelp[1]}\n'

        for key in commandtxt.keys():
            helptxt += '\n ---' + key + '---\n' + commandtxt[key]

        await ctx.send('```' + helptxt + '```');

    @commands.command(name="moeda", help="Misc:Retorna cara ou coroa.", alias=['coin', 'toss', 'caracoroa'])
    async def moeda(self, ctx):
        toss = 'cara' if (random() < .5) else 'coroa';
        await ctx.send('```' + ctx.message.author.name + ' tirou ' + toss + '```')

    @commands.command(name="escolha", help="Misc:Retorna um dos parametros passados (separar com ;).", alias=['choose', 'pickfrom'])
    async def escolha(self, ctx):
        choices = ctx.message.content.split(" ", 1)[1]
        choices = re.sub(' +', ' ', choices).split(";")
        index = self.RandomIndex(len(choices))
        await ctx.send('```' + choices[index] + '```')

    @commands.command(name="bicho", help="Misc:Animal do dia.", alias=['animal'])
    async def bicho(self, ctx):
        if self.today != date.today():
            self.today = date.today()
            self.randomValue = random()

        animals = ['1-Avestruz','2-Águia','3-Burro',
                   '4-Borboleta','5-Cachorro','6-Cabra',
                   '7-Carneiro','8-Camelo','9-Cobra','10-Coelho',
                   '11-Cavalo','12-Elefante','13-Galo','14-Gato',
                   '15-Jacaré','16-Leão','17-Macaco','18-Porco',
                   '19-Pavão','20-Peru','21-Touro','22-Tigre',
                   '23-Urso','24-Veado','25-Vaca']

        await ctx.send('```' + animals[math.floor(self.randomValue * len(animals))] + '```')

def setup(client):
    client.add_cog(misc(client))
