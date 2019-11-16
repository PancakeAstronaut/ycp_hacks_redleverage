import discord
from globals import API_INFO
from language_analysis import language_evaluation
from language_analysis import sentiment_analysis
from miniGames import jokehaus
from language_analysis import banHammer
from database import database_query


class MyClient(discord.Client):

    async def show_warning(self, message, strikes):
        print(strikes)
        weekly_strikes = strikes['week']
        monthly_strikes = strikes['month']
        channel = message.channel
        sender = message.author.mention
        warning = "You used banned language, Don't get banned!"
        await channel.send(sender + ": " + warning + " & " + "You have {} strikes this week, and {} stikes this month".format(weekly_strikes, monthly_strikes))

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
        channel = message.channel
        sender = message.author.mention
        isbanned_lang = banHammer.ban_tunnel(message.content)
        if isbanned_lang:
            strikes = database_query.add_strike(message.author.id)
            await self.show_warning(message, strikes)
        if message.content == "!joke":
            await self.jokehandler(message)
        elif message.content == "!riddle":
            await self.riddlemethis(message)
        elif str("<@645071848874180649>") in message.content:
            var = message.content.split(">")
            if message.author == client.user:
                pass
            else:
                message_swap = '{}'.format(var[1])
                sentiment_polarity = sentiment_analysis.get_sentiment(message_swap)
                database_query.update_polarity(message.author.id, sentiment_polarity)
                tone = language_evaluation.get_chat_tone(database_query.get_polarity(message.author.id))
                auto_response = language_evaluation.response_handler(tone)
                await channel.send(sender + " || " + auto_response)
                print('Message from {}: {}'.format(message.author, var[1]))
                print("Auto Response: {}".format(auto_response))
                print('Tone was: {} and Sentiment Polarity was: {}'.format(tone, sentiment_polarity))
                print("-----------------------------------------------------------------------------")


client = MyClient()
client.run(API_INFO.TOKEN)
