import discord
from globals import API_INFO
from language_analysis import language_evaluation
from language_analysis import sentiment_analysis
from miniGames import jokehaus
from language_analysis import banHammer


class MyClient(discord.Client):

    async def show_warning(self, message):
        channel = message.channel
        warning = "You used banned language, Don't get banned!"
        await channel.send(warning)

    async def riddlemethis(self, message):
        channel = message.channel
        riddle = jokehaus.get_riddle()
        await channel.send(riddle)

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
        isbanned_lang = banHammer.ban_tunnel(message.content)
        if isbanned_lang:
            await self.show_warning(message)
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
                auto_response = language_evaluation.response_handler(tone)
                print('Message from {0.author}: {0.content}'.format(message))
                print("Auto Response: {}".format(auto_response))
                print('Tone was: {} and Sentiment Polarity was: {}'.format(tone, sentiment_polarity))
                print("-----------------------------------------------------------------------------")


client = MyClient()
client.run(API_INFO.TOKEN)
