#importing discord package
import discord
import asyncio
import datetime
from discord.ext import commands, timers

bot = commands.Bot(command_prefix= '.') #our bot
bot.timer_manager = timers.TimerManager(bot)

@bot.event 
#the bot does certian actions when event occurs
async def on_ready():
    general_channel = bot.get_channel(777078774659022862)
    await general_channel.send('Hi!') 
    await general_channel.send('Would you like to study with me?')  

@bot.event
async def on_message(message):
    if message.content == 'I cannot focus':
        general_channel = bot.get_channel(777078774659022862)
        await general_channel.send('That is ok. Take a 15 minute break and try again.')

@bot.command(name="timer")
async def timer(ctx, time, *, text):
    date = datetime.datetime(*map(int, time.split("/")))
    bot.timer_manager.create_timer("timer", date, args=(ctx.channel.id, ctx.author.id, text))
    # or without the manager
    timers.Timer(bot, "timer", date, args=(ctx.channel.id, ctx.author.id, text)).start()

@bot.event
async def on_reminder(channel_id, author_id, text):
    general_channel = bot.get_channel(777078774659022862)

    await general_channel.send("Hey, <@{0}>, remember to: {1}".format(author_id, text))


#run the client on the server
bot.run('Nzc3MDU1NDAyODIyMzM2NTQ0.X693PQ.qoHRcy1DxiFx4Y1CqF8eZHDRPvQ')
