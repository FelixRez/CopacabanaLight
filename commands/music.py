import discord
from discord.ext import commands,tasks

from Player import Player


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

        #all the music related stuff
        self.player = Player()
        self.check.start()

    @commands.command(name="tocar", help="Music:Toca uma musica do YouTube",aliases=['p','play'])
    async def tocar(self, ctx, *args):
        try:
            voice_channel = ctx.author.voice.channel
        except:
            await ctx.send(embed=discord.Embed(colour=12255232, description='Voce nao esta conectado em nenhum canal..'))
            return
        else:
            await self.player.setvoicechannel(voice_channel)
            query = " ".join(args)
            song = self.player.add(query)

            if not song[0]:
                await ctx.send(embed=discord.Embed(colour=12255232, description='Nada foi encontrado'))
                return

            await ctx.send(embed=discord.Embed(colour=32768, description=f"{song[1]} adicionada"))
            if not self.player.is_playing:
                self.player.play()

    @commands.command(name="fila", help="Music:Lista de musicas adicionadas.",aliases=['q','queue'])
    async def fila(self, ctx):
        queue = self.player.queue()
        await ctx.send(queue)

    @commands.command(name="pular", help="Music:Pular musica.",aliases=['s','skip'])
    async def pular(self, ctx):
        self.player.skip()

    @commands.command(name="parar", help="Music:Para de tocar e limpa a lista de musicas.",aliases=['stop'])
    async def parar(self, ctx):
        self.player.stop()
        self.player.clear()

    @tasks.loop(seconds=60)
    async def check(self):
        if self.player.done():
            await self.player.disconnect()

def setup(client):
    client.add_cog(music(client))
