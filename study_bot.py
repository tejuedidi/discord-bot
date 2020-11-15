#importing discord package
import discord
import random
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix = '.')

token = open("token.txt", "r").read() 

@client.event 
#the bot does certian actions when event occurs
async def on_ready():
    print('Bot is online')

# @bot.event
@client.event 
async def on_message(message):
    testing_channel = client.get_channel(777020572008841216)
    if message.content == 'I can\'t focus':
        await testing_channel.send('That\'s okay. Take a 15 minute break and try again.')
    elif message.content == 'I\'m feeling unmotivated':
         motiv_message = ['Once you\'re done with work, you can just relax!',
                          'Work for ten more minutes, then take a short break. You\'d have earned it!',
                          'C\'mon. Just one more assignment, then you\'ll be free!',
                          'You\'ve got this. Persevere, and you\'ll be more thankful for yourself because of it!',
                          'You\'re so close to being done! Just one more assignment!']
    await testing_channel.send(random.choice(motiv_message))

client.run(token)