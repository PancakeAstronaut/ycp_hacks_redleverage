import discord
from globals import API_INFO


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in client.guilds:
            if guild.name == API_INFO.GUILD:
                print(f'{self.user} is connected to {guild.name}(id: {guild.id})')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run(API_INFO.TOKEN)
