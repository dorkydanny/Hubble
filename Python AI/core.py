from nextcord.ext import commands
from nextcord.ext import *
import discord
import nextcord
import random
import json
from os import path

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=';', intents=intents, help_command=None)


@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    
    emb = nextcord.Embed(title=f"Hubble has a latency of {ping}ms", description="type ;help for more commands",  color=nextcord.Color.orange())
    await ctx.send(embed=emb)

    
@bot.event
async def on_ready():
    global listObj
    global d
    global filename
    global earn_filename
    global jsonString
    activity = nextcord.Game(name=";help", type=2)
    await bot.change_presence(status=nextcord.Status.do_not_disturb, activity=activity)
    print(f"I is ready!")
    listObj = []
    filename = 'Python AI/users.json'
    earn_filename = 'Python AI/earn.json'
    if path.isfile(filename) is False:
        raise Exception("File not found")
    with open(filename) as fp:
        listObj = json.load(fp)
    for i in listObj:
        jsonString = str(i).replace("\'", "\"")
        d = json.loads(jsonString)
@bot.command()
async def earn(ctx):
    global earn_filename
    global listObj2
    listObj2 = []
    with open(earn_filename) as fp2:
        listObj2 = json.load(fp2)
    
    global guild_earn
    global ans
    global person
    global asked
    guild_earn = ctx.guild.id
    person = ctx.author
    man = ctx.author
    man = str(man)
    global jsonString
    global dam
    global listObj
    
    for i in range(len(listObj)):
        jsonThing = str(listObj[i]).replace("\'", "\"")
        d = json.loads(jsonThing)    
        if len(d) != 0:
            if man in d:
                math1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                math2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                choice1 = random.choice(math1) 
                choice2 = random.choice(math2)
                ans = choice1 * choice2
                ansemb = nextcord.Embed(title="Your Question Is:", description=f"{choice1}*{choice2}", color=discord.Color.orange())
                await ctx.send(embed=ansemb)
                
                
                for i in range(len(listObj2)):
                    jsonThing = str(listObj2[i]).replace("\'", "\"")
                    da = json.loads(jsonThing)
                    derp = str(ctx.guild.id)
                    if str(ctx.guild.id) in listObj2[i]:
                        listObj2[i][derp] = ans
                        
                with open(earn_filename, 'w') as json_file2:
                    json.dump(listObj2, json_file2)
                break
    
            else:
        
                await ctx.reply('You are not registered. Type **;r** or **;register** to register')
                
                
    
    
    isExists2 = False
    for i in listObj2:
        jsonString = str(i).replace("\'", "\"")
        dis = json.loads(jsonString)
        
        if len(dis) > 0:
                
            if str(ctx.guild.id) in dis:
                isExists2= True
                break
    if not isExists2:
            
            
        listObj2.append({
            f"{ctx.guild.id}" : ans
        })
        
        
        
        
    with open(earn_filename, 'w') as json_file:
        json.dump(listObj2, json_file, 
                        indent=4,  
                        separators=(',',': '))
    await ctx.send(ctx.guild.id)
        
@bot.command()
async def answer(ctx, message):
    global listObj2
    global person
    global ans
    global asked
    global guild_earn
    await ctx.send(ctx.guild.id)
    
        
    
    message = str(message)
    for i in range(len(listObj2)):
        jsonThing = str(listObj2[i]).replace("\'", "\"")
        da = json.loads(jsonThing)
        derp2 = str(ctx.guild.id)
        if str(ctx.guild.id) in listObj2[i]:
            if message in str(listObj2[i][derp2]):
                if message == str(listObj2[i][derp2]):
                    man = ctx.author
                    man = str(man)
                    for i in range(len(listObj)):
                        jsonThing = str(listObj[i]).replace("\'", "\"")
                        da = json.loads(jsonThing)
                        if man in listObj[i]:
                            v = listObj[i][man]
                            taomiteir = random.randint(0, 20) 
                            listObj[i][man] = v + taomiteir
                    with open(filename, 'w') as json_file:
                        json.dump(listObj, json_file)
                    trueembed = nextcord.Embed(title=f'You are correct, you have earned {taomiteir} wisdom', description='Type ``;earn`` for another go', color=discord.Color.green())
                    await ctx.send(embed=trueembed)
                    ans = random.randint(0, 10000)
                    for i in range(len(listObj2)):
                        jsonThing = str(listObj2[i]).replace("\'", "\"")
                        da = json.loads(jsonThing)
                        derp2 = str(ctx.guild.id)
                        if str(ctx.guild.id) in listObj2[i]:
                            listObj2[i][derp2] = ans
                        
                with open(earn_filename, 'w') as json_file2:
                    json.dump(listObj2, json_file2)
                    break
            if message not in str(listObj2[i][derp2]):
                wrongembed = nextcord.Embed(title='You are wrong', description='Type ``;earn`` for another go!', color =discord.Color.red())
                await ctx.reply(embed=wrongembed)
                ans = random.randint(0, 10000)
                for i in range(len(listObj2)):
                    jsonThing = str(listObj2[i]).replace("\'", "\"")
                    da = json.loads(jsonThing)
                    derp2 = str(ctx.guild.id)
                    if str(ctx.guild.id) in listObj2[i]:
                        listObj2[i][derp2] = ans
                with open(earn_filename, 'w') as json_file2:
                    json.dump(listObj2, json_file2)
                    break
                
        
            
            
            
                            
@bot.command(aliases=['r'])
async def register(ctx):
    global filename
    global listObj
    global d
    filename = 'Python AI/users.json'
    listObj = []
    if path.isfile(filename) is False:
        raise Exception("File not found")
    with open(filename) as fp:
        listObj = json.load(fp)
    isExists = False
    for i in listObj:
        jsonString = str(i).replace("\'", "\"")
        d = json.loads(jsonString)
        if len(d) > 0:
                  
            if 'dorkydanny#6515' in d:
                isExists= True
                break
    if not isExists:
        await ctx.reply('You have been succesfully registered! Type **;earn** to start earning wisdom!')
        listObj.append({
            f"{ctx.author}" : 1
        })
    if isExists:
        await ctx.reply('You are already registered! Type **;earn** to start earning wisdom!')
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))    
@bot.command(aliases=['balance', 'b'])
async def bal(ctx, *, man: discord.Member):
    man = str(man)
    global jsonString
    global dam
    global listObj
    for i in listObj:
        jsonString = str(i).replace("\'", "\"")
        d = json.loads(jsonString)    
        if len(d) != 0:
            if man in d:
                manembed = nextcord.Embed(title=f"{man}'s Balance:", description=f'**{d[man]} wisdom**', color=discord.Color.orange())
                await ctx.send(embed=manembed)
@bot.command()
async def give(ctx, *, man: discord.Member):
    man = str(man)
    for i in range(len(listObj)):
        jsonThing = str(listObj[i]).replace("\'", "\"")
        da = json.loads(jsonThing)
        if man in listObj[i]:
            v = listObj[i][man]
            
            listObj[i][man] = v + 100
            
    
                        
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file)         
@bot.command()
async def poll(ctx,*,message):
    await ctx.message.delete()
    emb=discord.Embed(description=f"New Poll by @{ctx.author.display_name}", title=f"{message}",colour=discord.Color.orange())
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')   
@bot.command()
async def help(ctx):
    embed = nextcord.Embed(title='Help Commands For Hubble:', description='**https://bit.ly/HubbleBot**', color=discord.Color.orange())
    embed.add_field(name=";ping", value="Returns Hubble's latency", inline=False)
    embed.add_field(name=';earn', value="Earns wisdom", inline=False)
    embed.add_field(name=';register', value="Registers the user", inline=False)
    embed.add_field(name=";balance 'user'", value="Checks the users balance", inline=False)
    await ctx.send(embed=embed)

        
bot.run('ODg4NjIyNzQwNjk1ODE4Mjgw.YUVYaw.IkJMqSR2hTFjvMQitJeowAug5Ws')