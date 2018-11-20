# Work with Python 3.6
import discord
import sys
import random
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = sys.argv[1]

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.command(name="hello", brief="Say hello to the bot!", pass_context=True)
async def hello(context):
    possible_responses = ["Hello", "Greetings", "Well met", "Hi there", "What's up"]
    await bot.say(random.choice(possible_responses) + " " + context.message.author.mention)

@bot.command(name="newCharacter",
             brief="Create a new character",
             pass_context=True,
             description="Will assign your account a new character. Won't do anything if you already have a character.",
             aliases = ["newChar"])
async def newCharacter(context):
    lst = context.message.content.split()
    lst = lst[1:]
    if(len(lst) == 0):
        return await bot.say("`!newCharacter <name>`")

    name = ""
    for i in lst:
        name += i

    if(len(name) > 16):
        return await bot.say("`Your character's name must not exceed 16 characters`")
    elif(not name.isalpha()):
        return await bot.say("`Your character's name must contain only letters`")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)