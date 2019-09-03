# Work with Python 3.6
import sys
import random
from src.Healer import Healer
from src.DPS import DPS
from src.Tank import Tank
from src.CharacterDB import CharacterDB
from discord.ext import commands

BOT_PREFIX = "!"
TOKEN = sys.argv[1]
characterDB = CharacterDB()

bot = commands.Bot(command_prefix=BOT_PREFIX)


def trimContext(context):
    # Trim the front off of the context and return the remainder of the string
    string = ""
    lst = context.message.content.split()
    lst = lst[1:]
    for i in lst:
        string += str(i)
    return string


@bot.command(name="hello", brief="Say hello to the bot!", pass_context=True)
async def hello(context):
    possible_responses = ["Hello", "Greetings", "Well met", "Hi there", "What's up"]
    await context.send(random.choice(possible_responses) + " " + context.message.author.mention)


@bot.command(name="newCharacter",
             brief="Create a new character",
             pass_context=True,
             description="Will assign your account a new character. Won't do anything if you already have a character.",
             aliases = ["newChar", "newcharacter", "newchar"])
async def newCharacter(context):
    # Break off thee command text from the message, make sure it's valid
    string = trimContext(context)
    nameAndRole = string.split(",")

    # Error check the list to make sure it doesn't have a comma
    if(len(string) == 0 or len(nameAndRole) != 2):
        return await context.send("`!newCharacter <name>, <Healer, Tank, DPS>`")

    name = nameAndRole[0]
    role = nameAndRole[1].lower()

    # Error check the name to make sure it's not super long
    if(len(name) > 16):
        return await context.send("`Your character's name must not exceed 16 characters`")

    # Error check the name to make sure it's only characters
    elif(not name.isalpha()):
        return await context.send("`Your character's name must contain only letters`")

    # On valid input, make a character based on their role
    else:
        if(characterDB.isInDB(name)):
            return await(context.send("`There already exists a character with that name. Please choose another`"))

        if(role == "dps"):
            # Make a DPS character
            char = DPS(name)
            characterDB.addToDB(char)
            return await context.send("`" + name + " created successfully, Role: DPS`")

        elif(role == "healer"):
            # Make a healer character
            char = Healer(name)
            characterDB.addToDB(char)
            return await context.send("`" + name + " created successfully, Role: Healer`")

        elif (role == "tank"):
            # Make a tank character
            char = Tank(name)
            characterDB.addToDB(char)
            return await context.send("`" + name + " created successfully, Role: Tank`")

        else:
            return await context.send("`" + role + " is not an acceptable role. Please choose DPS, Healer, or Tank.`")


@bot.command(name="stats",
             brief="Get stats of a character",
             pass_context=True,
             description="Display the stats of a character when given the name of the character",
             aliases = ["statistics"])
async def stats(context):
    name = trimContext(context)
    if(len(name) == 0):
        return await context.send("`No name was entered`")

    if(not characterDB.isInDB(name)):
        return await context.send("`Character '" + name + "' was not found in the database.`")

    return await context.send(characterDB.getCharacter(name).toString())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)