from discord.ext import commands
import math
from datetime import date,datetime
from random import random

class planeta(commands.Cog):
    def __init__(self, client):
        self.client = client

    def RandomIndex(self, arraySize):
        return math.floor(random() * arraySize)

    @commands.command(name="luiz", help="Planeta:Retorna fatos sobre Luiz.")
    async def luiz(self, ctx):
        #var days = Math.round((new Date() - new
        #Date('2021-09-18T00:00:00')) / 86400000);
        #const
        today = date.today()
        day = datetime.strptime('18/09/21 13:00:00', '%d/%m/%y %H:%M:%S').date()
        days = round(abs((today - day).days))
        phrases = [
            f'Luiz esta apaixonado faz {days} dias',
            'Luiz n quer mais saber de mulher!',
            'Luiz vai casar esse ano',
            f'Luiz so pensa nela faz {days} dias',
            f'Luiz esta planejando o casamento faz {days} dias',
            'Luiz \"LoL eh melhor que mulher\"'
        ]
        index = self.RandomIndex(len(phrases))
        await ctx.send('```' + phrases[index] + '```')

    @commands.command(name="uia", help="Planeta:Retorna quantos fios de cabelo Uia perdeu... :'(")
    async def uia(self, ctx):
        hairs = self.RandomIndex(1000)
        phrases = [
            'Hoje deus interveio e uia n perdeu seus cabelos, talvez eles um dia eles cresçam novamente :D',
            'Uia perdeu apenas 1 fio de cabelo hoje(eu definitivamente n fui pago para dizer isso)',
            f'Uia perdeu apenas {hairs} fios de cabelo hoje(eu definitivamente n fui pago para dizer isso)',
            f'Uia perdeu {hairs} fios de cabelo'
        ]
        index = 0
        if hairs == 1:
            index = 1
        elif hairs < 10:
            index = 2
        else:
            index = 3

        await ctx.send('```' + phrases[index] + '```')


def setup(client):
    client.add_cog(planeta(client))