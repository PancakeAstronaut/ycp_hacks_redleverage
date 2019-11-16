import discord
from globals import API_INFO
from language_analysis import language_evaluation
from language_analysis import sentiment_analysis
from miniGames import jokehaus


class MyClient(discord.Client):

    async def riddlemethis(self, message):
        chennel = message.channel
        riddle = jokehaus.get_riddle()
        await chennel.send(riddle)

    async def jokehandler(self, message):
        channel = message.channel
        joke = jokehaus.get_joke()
        await channel.send(joke)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in client.guilds:
            if guild.name == API_INFO.GUILD:
                print(f'{self.user} is connected to {guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.content == "!joke":
            await self.jokehandler(message)
        elif message.content == "!riddle":
            await self.riddlemethis(message)
        else:
            if message.author == client.user:
                pass
            else:
                message_swap = '{0.content}'.format(message)
                sentiment_polarity = sentiment_analysis.get_sentiment(message_swap)
                tone = language_evaluation.get_chat_tone(sentiment_polarity)
                print('Message from {0.author}: {0.content}'.format(message))
                print('Tone was: {} and Sentiment Polarity was: {}'.format(tone, sentiment_polarity))


client = MyClient()
client.run(API_INFO.TOKEN)
