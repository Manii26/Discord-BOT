from discord.ext import commands
import discord
from random import *


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 652839290325172224 # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

    

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    author = ctx.message.author
    await ctx.send(author.name)

@bot.command()
async def d6(ctx):
    n = randint(1,6)
    await ctx.send(n)

@bot.event
async def on_message(message):
    words = ['"Salut tout le monde"']

    if message.content in words: 
        await message.channel.send('"Salut tout seul"')


  
@bot.command(name='ban')
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Oh oh {ctx.author.mention} don't provide a reason!")
    else:
        the_message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(the_message)
        await member.ban(reason=reason)

@bot.tree.command()
async def xkcd(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://xkcd.com/2674/")

    await interaction.response.send_message(embed=embed) 

token = ""
bot.run(token)  # Starts the bot


