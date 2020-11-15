#importing discord package
import discord
import random
import datetime
from discord.ext import commands, tasks
from random import choice

bot = commands.Bot(command_prefix = '~')
token = open("token.txt", "r").read() 

@bot.event 
#the bot does certain actions when event occurs
async def on_ready():
    print('Bot is online')
    testing_channel = bot.get_channel(777020572008841216)
    await testing_channel.send('Hello there :)')

@bot.event
async def on_message(message):
    testing_channel = bot.get_channel(777020572008841216)
    if message.content == 'I can\'t focus': 
        await testing_channel.send('That\'s okay. Take a 7 minute break and try again.')
    elif message.content == 'I am ready to finish some work!': 
        await testing_channel.send('Awesome! Hone in that energy till the end.')
    elif message.content == 'I am tired but I have so much work':
        a_message = ['C\'mon. Just one more assignment, then you\'ll be free!',
                     'You\'re so close to being done! Let\'s finish strong!',]
        await testing_channel.send(random.choice(a_message))
    elif message.content == 'I don\'t feel like doing work':
        motiv_message = ['Once you finish you\'re work you can relax!',
                        'Work in small intervals at a time. How about we try to stay focused for 15 minutes? Then take a short break, you earned it!',
                        'You\'ve got this. Persevere, and you\'ll be more thankful for yourself because of it!',]
        await testing_channel.send(random.choice(motiv_message))
    elif message.content == '~study':
        embedVar1 = discord.Embed(title = "Study links", description = " ", color = 0x4D71A5)
        embedVar1.add_field(name = "Science :test_tube:", value = "[Khan Academy](https://www.khanacademy.org/science)", inline = False)
        embedVar1.add_field(name = "Computing :computer:", value = "[Khan Academy](https://www.khanacademy.org/computing)", inline = False)
        embedVar1.add_field(name = "Math :abacus:", value = "[Khan Academy](https://www.khanacademy.org/math)", inline = False)
        embedVar1.add_field(name = "Arts & Humanities :scales:", value = "[Khan Academy](https://www.khanacademy.org/humanities)", inline = False)
        embedVar1.add_field(name = "Reading & Language Arts :bookmark:", value = "[Khan Academy](https://www.khanacademy.org/ela)", inline = False)
        embedVar1.add_field(name = "Economics :money_with_wings:", value = "[Khan Academy](https://www.khanacademy.org/economics-finance-domain)", inline = False)
        embedVar1.add_field(name = "Life Skills :bulb:", value = "[Khan Academy](https://www.khanacademy.org/college-careers-more)", inline = False)
        await message.channel.send(embed = embedVar1)
    elif message.content =='~distract':
        distract_pic = [
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\doggo-1.png'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\doggo-2.png'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\doggo-3.jpg'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\catto-1.jpg'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\catto-2.jpg'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\ham-1.jpg'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\hedge.png'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\ham-1.jpg'),]
        await testing_channel.send(file=choice(distract_pic))
    elif message.content =='~study meme':
        meme_pic = [
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\meme-1.jpeg'),
            discord.File(r'C:\Users\tejue\Desktop\Creatica\discord-bot\images\meme-2.png'),]
        await testing_channel.send(file=choice(meme_pic))
    elif message.content == '~help':
        embedVar2 = discord.Embed(title = "StudyBuddy prompts", description = " ", color = 0x4D71A5)
        embedVar2.add_field(name = "Helps with studying", value = "`~study`", inline = False)
        embedVar2.add_field(name = "Displays brief distractions", value = "`~distract`", inline = False)
        embedVar2.add_field(name = "Memes. Need I say more?", value = "`~study meme`", inline = False)
        embedVar2.add_field(name = "Break reminders", value = "`I can\'t focus`", inline = False)
        embedVar2.add_field(name = "Encouragement to move forward", value = "`'I am tired but I have so much work'`", inline = False)
        embedVar2.add_field(name = "An uplifting message", value = "`'I don\'t feel like doing work'`", inline = False)
        embedVar2.add_field(name = "Continued motivation", value = "`'I am ready to finish some work!'`", inline = False)
        await message.channel.send(embed = embedVar2)

bot.run(token)