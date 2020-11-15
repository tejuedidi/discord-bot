#importing discord package
import discord
import asyncio
import datetime
import random
from discord.ext import commands

bot = commands.Bot(command_prefix= '.') #our bot

@bot.event 
#the bot does certain actions when event occurs
async def on_ready():
    testing_channel = bot.get_channel(777020572008841216)
    await testing_channel.send('Hi!') 
    await testing_channel.send('Would you like to study with me?')  

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

#run the client on the server
bot.run('Nzc3MjQ3MDEwOTIyNDMwNDg1.X7Aprw.DlA8zn2LBdNA_AV_C-yU_izGuaY')