import discord


GUILD = "Red Leverage"



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in client.guilds:
            if guild.name == GUILD:
                print(f'{self.user} is connected to {guild.name}(id: {guild.id})')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('NjQ1MDcxODQ4ODc0MTgwNjQ5.Xc9lAw.7PW6MIVbTrvUGoKsth9-9ovISw8')
