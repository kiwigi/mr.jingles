#Mr.Jingles is your friend

import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix='pspsps ')

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
second = current_time.tm_sec

@client.event
async def on_ready():
    if hour == 3 :
        await ctx.send('*TIME 2 HAB LUNCH*')

@client.event
async def on_ready():
    print('mr.jingles is ready to snack...')

#help
@client.command(name='commands')
async def come(ctx):
    await ctx.send('COMMANDS:\n salami: What does Mr.Jingles think about salami? \n come: Mr jingles will come to you  \n snack: yummy \n feed: Feed Mr.Jingles \n pet: Give Mr.Jingles some love!\n talk: Mr.Jingles can talk! Come on, try it out!\n gotobed:Tells you to go to sleep.')

#salami
@client.command(name='salami')
async def salami(ctx):
    await ctx.send('MEOW meow meoew MOEWEOW!! Translation: cats can have a lil salami as a snack..')

#send media 
@client.command(name='selfie')
async def selfie(ctx):
    await ctx.send("*Mr.Jingles is looking rather dapper today.*")
    await ctx.send(file=discord.File('jjingle.jpg'))

#snack
@client.command(name='snack')
async def snack(ctx):
    await ctx.send('*Mr.Jingles looks at you! It looks like he is asking for an additional snack..*')

#come
@client.command(name='come')
async def come(ctx):
    await ctx.send('*Mr.Jingles looks at you and lays down.*')

#goodnight
@client.command(name='goodnight')
async def come(ctx):
    await ctx.send('*Its time to sleep. Mr.Jingles curls up to your head as he purrs. Your head feels nice and cozy! Mr.Jingles closes his eyes.\nGoodnight Mr Jingles.*')

#feed menu and options
@client.command(name='feed')
async def feed(ctx):
    #await ctx.send('What would you like to feed Mr.Jingles?')
    await ctx.send('Whats on the menu??\nSALAMI: feed salami\nTUNA: feed tuna\nVEGTABL: feed vegtabl\nlööps: feed fruitloops')
    @client.event
    async def on_message(message):
        auth = message.author
        if message.author == client.user:
            return
        if message.author == auth:
            if message.content== 'feed salami':
                await ctx.send('*Mr.Jingles looks happy. He is grateful for a lil salami. Although he would like more, he knows that cats can only have a little salami as a snack so he goes to sleep instead of asking for more. Good job Mr.Jingles!*')
                await client.process_commands(message)
            elif message.content== 'feed tuna':
                await ctx.send('*Mr.Jingles looks happy but meows.. Maybe he wants more?*')
                await client.process_commands(message)
            elif message.content== 'feed vegtabl':
                await ctx.send('*Mr.Jingles does not eat such fowl things! He leaves and never speaks to you again!*')
                await client.process_commands(message)
            elif message.content== 'feed fruitloops':
                await ctx.send('*Mr.Jingles feeds on the loops...*')
                m=await ctx.send("MEOW!!!!")
                await ctx.send(content="Translation: Thank you for the lööps, brøther.")
                await client.process_commands(message)
            else:
                #await ctx.send("*that wasn't an option dummy*")
                await client.process_commands(message)
    await client.process_commands(message)

            
    
#pet...
@client.command(name='pet')
async def pet(ctx):
    petOps = ['*Mr.Jingles does a backflip.*','*Mr.Jingles starts purring. Awww*', '*OH NO! Mr.Jingles scratched you.. You are losing a lot of blood... Your vision goes black!! You close your eyes. In your final moments, you think to yourself: it was worth it.*']
    await ctx.send(random.choice(petOps)) 

#talks to the chat
@client.command(name='talk')
async def come(ctx):
    await ctx.send('meow', tts=True)

#talks to the chat - go to bed!
@client.command(name='gotobed')
async def come(ctx):
    await ctx.send('ITS PAST YOUR BEDTIME', tts=True)


#token
client.run('token goes here ')