from discord.ext import commands
import discord
from discord import *
import asyncio
import random
import json
from discord_components import *
client = commands.Bot(command_prefix=".")

client.remove_command('help')
player1 = ""
player2 = ""
turn = ""
gameOver = True
fun = "https://www.thisworldthesedays.com/minecraft-website.html"
global warnings
warnings = 0
board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
    print(f"Bot is ready as {client.user}")
    DiscordComponents(client)
@client.command()
async def openlink(ctx, pagelink):
    page = pagelink
    if pagelink == 'yt':
        page = ('https://www.youtube.com/')
    elif pagelink == 'reddit':
        page = ("https://www.reddit.com/")
    elif pagelink == "discordapi":
        page = ("https://discordpy.readthedocs.io")
    else:
        page=(f"https://{pagelink}.com")    
    embed=discord.Embed(title="Your link", url=page, colour=discord.Colour.orange())
    await ctx.send(embed=embed)
@client.command()
async def hello(ctx):
    await ctx.send(f"Greetings, {ctx.author}") 
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers!")
    activeservers = client.guilds
    for guild in activeservers:
        await ctx.send(guild.name)
        print(guild.name)
@client.command()
async def add(ctx, num1:int, num2:int):
    await ctx.send(num1+num2) 
@client.command()
async def poll(ctx,*,message):
    emb=discord.Embed(title=f"New Poll by @{ctx.author.display_name}", description=f"{message}",colour=discord.Color.orange())
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")

@client.command(aliases=['8ball'])
async def eight_ball(ctx, *, question):
    responses = ['Yes', 'No', 'I dont know']
    emb=discord.Embed(title=f"Question: {question}",description=f'Answer: {random.choice(responses)}', colour = discord.Colour.orange())
    await ctx.send(ctx.message.author, embed=emb)
@client.command()
async def test(ctx):
    await ctx.send(f"Bot up and runnings as {client.user}, message sent by {ctx.author}, please type .help for commands")
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")


@client.command()
async def stopgame1(ctx):
    
    global gameOver
    gameOver=True
    embed = discord.Embed(title="game stopped", colour= discord.Colour.orange())
    await ctx.send(embed=embed)
    
@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command()
async def emojify(ctx, *, text):
    emojis = []  
    for s in text.lower():
        if s.isdecimal():
            num2emo = {'0':'zero', 
                       '1':'one', 
                       '2':'two', 
                       '3':'three', 
                       '4':'four', 
                       '5':'five', 
                       '6':'six', 
                       '7':'seven', 
                       '8':'eight', 
                       '9':'nine'}
            emojis.append(f':{num2emo.get(s)}:') 
        elif s.isalpha():
            emojis.append(f':regional_indicator_{s}:')
        else:
            emojis.append(s)
    await ctx.send(' '.join(emojis))
@client.command()
async def planeidea(ctx, *, idea):
    channel = client.get_channel(745080427709988874)
    embed = discord.Embed(title=f'Plane idea by {ctx.message.author.display_name}',description=f'Idea: {idea}',colour = discord.Color.orange())
    
    await channel.send(embed=embed)  
@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message):
    channel = client.get_channel(745080120099995671)
    await channel.send(message) 
                 
@client.command()
async def code(ctx, language, *,code):
    embed = discord.Embed(title=f"Code by {ctx.author.display_name}", description=f"```{language}\n{code}\n```", colour = discord.Colour.orange())
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx):
    warnings += 1
@client.command()
@commands.has_permissions(manage_messages=True)
async def warning(ctx):
    await ctx.send(warnings)
    
    
    

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name="Help")
    embed.add_field(name=".tictactoe 'player1' 'player2'", value="starts a game of tictactoe between two players", inline=False)
    embed.add_field(name='.ping', value="Returns the bot's latency", inline=False)
    embed.add_field(name='.test', value="Returns test results of bot", inline=False)
    embed.add_field(name='.code', value="Type language, then code", inline=False)
    embed.add_field(name=".openlink 'abreviated link'", value="Gives you link in an embed", inline=False)
    embed.add_field(name=".8ball 'question'", value="Predicts the answer of your question", inline=False)
    embed.add_field(name=".poll 'question'", value="Creates a poll with your question", inline=False)
    embed.add_field(name=".add 'num1' 'num2'", value="Adds your two numbers together", inline=False)
    embed.add_field(name='.hello', value="Replies with hello", inline=False)
    await ctx.send(author, embed=embed)
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def dashboard(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name="Mod Menu")
    embed.add_field(name=".players", value="How much people in this guild", inline=False)
    
    await ctx.send(author, embed=embed)    
@client.command(pass_context=True)
async def invite(ctx) :
        embed = discord.Embed(
            color= discord.Colour.dark_teal() # or any color you want
        )
        embed.add_field(name='To Add Me To Your Server:' ,value='[Click Here!](https://bit.ly/HubbleBot)', inline=False)
        await ctx.send(embed=embed)
        
    
                
client.run('ODg4NjIyNzQwNjk1ODE4Mjgw.YUVYaw.IkJMqSR2hTFjvMQitJeowAug5Ws')