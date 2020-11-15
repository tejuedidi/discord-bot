#importing discord package
import discord
import random
from discord.ext import commands, tasks
from random import choice

bot = commands.Bot(command_prefix = '.')
token = open("token.txt", "r").read() 

@bot.event 
#the bot does certain actions when event occurs
async def on_ready():
    print('Bot is online')

@bot.event
async def on_message(message):
    testing_channel = bot.get_channel(777020572008841216)
    if message.content == 'I can\'t focus':
        await testing_channel.send('That\'s okay. Take a 15 minute break and try again.')
    elif message.content == 'I\'m feeling unmotivated':
        motiv_message = ['Once you\'re done with work, you can just relax!',
                        'Work for ten more minutes, then take a short break. You\'d have earned it!',
                        'C\'mon. Just one more assignment, then you\'ll be free!',
                        'You\'ve got this. Persevere, and you\'ll be more thankful for yourself because of it!',
                        'You\'re so close to being done! Just one more assignment!']
        await testing_channel.send(random.choice(motiv_message))
    elif message.content == '!study help':
        embedVar = discord.Embed(title = "Study links", description = " ", color = 0x4D71A5)
        embedVar.add_field(name=":test_tube:", value="[Science](https://www.khanacademy.org/science)", inline=False)
        embedVar.add_field(name=":computer:", value="[Computing](https://www.khanacademy.org/computing)", inline=False)
        embedVar.add_field(name=":abacus:", value="[Math](https://www.khanacademy.org/math)", inline=False)
        embedVar.add_field(name=":scales:", value="[Arts & Humanities](https://www.khanacademy.org/humanities)", inline=False)
        embedVar.add_field(name=":bookmark:", value="[Reading & Language Arts](https://www.khanacademy.org/ela)", inline=False)
        embedVar.add_field(name=":money_with_wings:", value="[Economics](https://www.khanacademy.org/economics-finance-domain)", inline=False)
        embedVar.add_field(name=":bulb:", value="[Life Skills](https://www.khanacademy.org/college-careers-more)", inline=False)
        await message.channel.send(embed = embedVar)

bot.run(token)