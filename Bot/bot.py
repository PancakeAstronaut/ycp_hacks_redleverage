import discord
from globals import API_INFO
from language_analysis import language_evaluation
from language_analysis import sentiment_analysis
from miniGames import jokehaus
from language_analysis import banHammer
from database import database_query


class MyClient(discord.Client):

    async def nice_meter(self, message, usr_id_mentions):
        channel = message.channel
        for user in usr_id_mentions:
            avg_polarity = database_query.get_polarity(user)
            current_tone = language_evaluation.get_chat_tone(avg_polarity)
            if current_tone == "Positive":
                nice_meter = "<@{}> is a Nice Person\n" \
                             "Their Average Sentiment is {}\n" \
                             "Their Overall Tone is {}".format(user, round(avg_polarity, 2), current_tone)
            elif current_tone == "Negative":
                nice_meter = "<@{}> is a Negative Norbert/Nancy\n" \
                             "Their Average Sentiment is {}\n" \
                             "Their Overall Tone is {}".format(user, round(avg_polarity, 2), current_tone)
            else:
                nice_meter = "<@{}> is an Average Joe/Jane\n" \
                             "Their Average Sentiment is {}\n" \
                             "Their Overall Tone is {}".format(user, round(avg_polarity, 2), current_tone)
            await channel.send(nice_meter)

    async def maze(self, message):
        channel = message.channel

    async def show_warning(self, message, strikes):
        weekly_strikes = strikes['week']
        monthly_strikes = strikes['month']
        channel = message.channel
        sender = message.author.mention
        warning = "You used banned language, Don't get banned!"
        await channel.send(sender + ": " + warning + " & " + "You have {} strikes this week, and {} strikes this month".format(weekly_strikes, monthly_strikes))

    async def riddlemethis(self, message):
        channel = message.channel
        riddle = jokehaus.get_riddle()
        await channel.send(riddle)

    async def jokehandler(self, message):
        channel = message.channel
        joke = jokehaus.get_joke()
        await channel.send(joke)

    async def wouldyourather(self, message):
        channel = message.channel
        wyr = jokehaus.get_wyr()
        await channel.send(wyr)

    async def truthbetold(self, message):
        channel = message.channel
        truth = jokehaus.get_truth()
        await channel.send(truth)

    async def doubledogdare(self, message):
        channel = message.channel
        dare = jokehaus.get_dare()
        await channel.send(dare)

    async def gettingnerdywithit(self, message):
        channel = message.channel
        dice = jokehaus.roll()
        await channel.send("Dice Roll Value: " + str(dice))

    async def beinghelpful(self, message):
        channel = message.channel
        embed = discord.Embed(
            title="Commands List!",
            description="Here are a list of all the commands for Red Leverage",
            colour=discord.Colour.green()
        )
        embed.add_field(name="!riddle", value="displays a riddle", inline=False)
        embed.add_field(name="!joke", value="displays a joke, more than likely a dad joke", inline=False)
        embed.add_field(name="!wyr", value="displays a would you rather question", inline=False)
        embed.add_field(name="!truth", value="displays a truth questions", inline=False)
        embed.add_field(name="!dare", value="displays a dare", inline=False)
        embed.add_field(name="!roll", value="displays a dice roll on a d20", inline=False)
        embed.add_field(name="!maze", value="displays a mini adventure ", inline=False)
        embed.add_field(name="!nm", value="shows nice meter for mentioned users", inline=False)
        await channel.send(content=None, embed=embed)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in client.guilds:
            if guild.name == API_INFO.GUILD:
                print(f'{self.user} is connected to {guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if "!nm" in message.content:
            usr_mentions = message.mentions
            usr_id_mentions = []
            for userid in usr_mentions:
                usr_id_mentions.append(userid.id)
            if len(usr_id_mentions) > 0:
                await self.nice_meter(message, usr_id_mentions)
        else:
            pass
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
        elif message.content == "!wyr":
            await self.wouldyourather(message)
        elif message.content == "!truth":
            await self.truthbetold(message)
        elif message.content == "!dare":
            await self.doubledogdare(message)
        elif message.content == "!roll":
            await self.gettingnerdywithit(message)
        elif message.content == "!help":
            await self.beinghelpful(message)
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
                # For Debugging only, Code Goes above
                # print('Message from {}: {}'.format(message.author, var[1]))
                # print("Auto Response: {}".format(auto_response))
                # print('Tone was: {} and Sentiment Polarity was: {}'.format(tone, sentiment_polarity))
                # print("-----------------------------------------------------------------------------")
        else:
            sentiment_polarity = sentiment_analysis.get_sentiment(message.content)
            database_query.update_polarity(message.author.id, sentiment_polarity)


client = MyClient()
client.run(API_INFO.TOKEN)
