import discord
from youtube_dl import YoutubeDL

class Player():
    def __init__(self):
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.voiceChannel = ""

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def add(self, query):
        song = self.search_yt(query)

        if type(song) == type(True):
            return [False, ""]

        self.music_queue.append(song)
        return [True, f"{song['title']}"]

    def done(self):
        return (not self.is_playing) and len(self.music_queue) <= 0

    def next(self):
        m_url = self.music_queue[0]['source']
        self.music_queue.pop(0)
        return discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS)

    def play(self):
        self.is_playing = len(self.music_queue) > 0 and self.isvoicechannelready()
        if self.is_playing:
            self.voiceChannel.play(self.next(), after=lambda e: self.play())

    def clear(self):
        self.music_queue.clear()

    async def setvoicechannel(self, channel):
        if channel == self.voiceChannel:
            return

        if self.isvoicechannelready() and self.voiceChannel.is_connected():
            await self.voiceChannel.move_to(channel)
        else:
            self.voiceChannel = await channel.connect()

    def isvoicechannelready(self):
        return self.voiceChannel != "" and self.voiceChannel

    def queue(self):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f'{i+1} - ' + self.music_queue[i]['title'] + "\n"

        if retval != "":
            return '```' + retval + '```'
        return '```Fila esta vazia.```'

    def skip(self):
        self.stop()
        self.play()

    def stop(self):
        if self.isvoicechannelready():
            self.voiceChannel.stop()

    async def disconnect(self):
        if self.isvoicechannelready():
            await self.voiceChannel.disconnect()
