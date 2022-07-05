from email import message
from lib2to3.pgen2 import token
import discord
from discord.ext import commands
import random
import time
import mysql.connector


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=['pspsps ', 'Pspsps '], intents=intents)

# inp = open('dbConn.txt', 'r', encoding='utf-8')

# connection = eval('mysql.connector.connect({})'.format(inp.readline().strip()))

# inp.close()



# current_time = time.localtime()
# hour = current_time.tm_hour
# minute = current_time.tm_min
# second = current_time.tm_sec



#@client.event
# @client.command(name='talk')
# async def on_ready():
#     print('mr.jingles is ready to snack...')

class MyView(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "What's on the menu?", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maxmimum number of values that can be selected by the users
        disabled = False,
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Salami",
                value="0",
                emoji="🍖",
                description="Cats can have a lil salami as a snack"
            ),
            discord.SelectOption(
                label="Tuna",
                value="1",
                emoji="🐟",
                description="A safe choice for a cat"
            ),
            discord.SelectOption(
                label="Vegtabl",
                value="2",
                emoji="🥦",
                description="You might want to re-think this"
            ),
            discord.SelectOption(
                label="froot loops",
                value="3",
                emoji="🍩",
                description="Is this healthy?"
            ),
            discord.SelectOption(
                label="Fancy Feast Wet Cat Food",
                value="4",
                emoji="🥫",
                description="A feast fit for a king"
            ),
            discord.SelectOption(
                label=" Hill's Science Diet Adult Urinary & Hairball Control Canned Cat Food, Savory Chicken Entrée, 5.5 oz",
                value="5",
                emoji="🥫",
                description="A healthier option"
            )
        ]
    )
    async def select_callback(ctx,select, interaction): # the function called when the user is done selecting options
  
        select.disabled = True
        
        if select.values[0] == "0":
            await interaction.response.send_message('*Mr.Jingles looks happy. He is grateful for a lil salami. Although he would like more, he knows that cats can only have a little salami as a snack so he goes to sleep instead of asking for more. Good job Mr.Jingles!* 🙌🥳')
            
        elif select.values[0] == "1":
            await interaction.response.send_message('*Mr.Jingles looks happy but meows.. Maybe he wants more?* 🥺')
         
        elif select.values[0] == "2":
            await interaction.response.send_message('🙀 *Mr.Jingles does not eat such fowl things! He leaves and never speaks to you again!* 😿💔')
          
        elif select.values[0] == "3":
            await interaction.response.send_message('*Mr.Jingles feeds on the loops...* "MEOW!!!!" \nTranslation: Thank you for the lööps, brøther.')
             
        elif select.values[0] == "4":
            await interaction.response.send_message('*Mr.Jingles looks pleased! He begins to serenade you by playing some Mozart on the cat piano* 🎶😳🎹')
            
        elif select.values[0] == "5":
            await interaction.response.send_message('*Mr.Jingles stares and wonders what you are trying to say by selecting the diet option. He does not look pleased.*')



@client.command(name= 'feed')
async def feed(ctx):
    authId = ctx.author.id
    message = await ctx.reply('Choose what to feed Mr.Jingles: ', view=MyView())
    #await ctx.send('<@'+str(authId)+'> has fed Mr.Jingles!')
    #await message.edit(content="A selection was made.")
    
 #catnip   
@client.command(name= 'catnip')
async def catnip(ctx):
    await ctx.send('🌿😎💨 *Mr.Jingles hits the nip...* ')
    nipOps = ['*AYO?! 😳 Mr.Jingles is break-dancing! The catnip went hard this time*','*Mr.Jingles looks super chill. He\'s straight-up just vibin right now. 😎*', '*Mr.Jingles speaks speaks to you. He says:*\nLong you live and high you fly\nSmiles you\'ll give and tears you\'ll cry\nAnd all you touch and all you see\nIs all your life will ever be.\n *I guess the catnip made his meow sound weird 😳*']
    await ctx.send(random.choice(nipOps)) 



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
    embed = discord.Embed(
        title="Mr.Jingles is looking rather dapper today.",
        color=discord.Colour.red()
        )
    embed.set_image(url="https://i.imgur.com/nqFuSaG.jpg")
    await ctx.send(embed=embed)   
    #await ctx.send(file=discord.File('jjingle.jpg'))

#snack
@client.command(name='snack')
async def snack(ctx):
    await ctx.send('*Mr.Jingles looks at you! It looks like he is asking for an additional snack..*')

#bitches
@client.command(name='bitches')
async def bitches(ctx):
    if ctx.author.id == 521931888378642443: #rochart
        await ctx.send('*Mr. Jingles is calling your bitches.... Oh wait, you have none!*')
        embed = discord.Embed(
                title="Hey Savage Fox,",
                color=discord.Colour.orange()
                )
        embed.set_image(url="https://i.kym-cdn.com/photos/images/original/002/297/373/9b2.gif")
        await ctx.send(embed=embed) 
    elif ctx.author.id == 760916060475228242: #liloozy
        await ctx.send('*Mr. Jingles is calling your bitches.... Oh wait, you have none!*')
        embed = discord.Embed(
                title="Hey LilOozy,",
                color=discord.Colour.purple()
                )
        embed.set_image(url="https://c.tenor.com/CQIMmoU_ipcAAAAC/no-bitches-bitches.gif")
        await ctx.send(embed=embed) 
    elif ctx.author.id == 363189216508903424: #mar
        await ctx.send('*Mr. Jingles is unable to call all of your bitches since you have too many.*')
        embed = discord.Embed(
                title="",
                color=discord.Colour.green()
                )
        embed.set_image(url="https://cdn.discordapp.com/attachments/940395109269254146/955675480403615784/AApV8ZE7Xwx4AAAAAElFTkSuQmCC.png")
        await ctx.send(embed=embed)
    elif ctx.author.id == 606141720563810315: #anna
        await ctx.send('*Mr. Jingles is unable to call all of your bitches since you have too many.*')
        embed = discord.Embed(
                title="",
                color=discord.Colour.green()
                )
        embed.set_image(url="https://cdn.discordapp.com/attachments/940849748330577983/955684098775609414/Felini_cat_summerTime_Sunnies_3k_orig-1024x683.png")
        await ctx.send(embed=embed)
    elif ctx.author.id == 807069645655244820: #gagan
        await ctx.send('*Mr. Jingles is unable to call all of your bitches since you have too many.*')
        embed = discord.Embed(
                title="",
                color=discord.Colour.green()
                )
        embed.set_image(url="https://cdn.discordapp.com/attachments/672162533670387855/955688800166756393/e107506570d16eb7f7cc01f2f51aaebc.png")
        await ctx.send(embed=embed)
    elif ctx.author.id == 96425998089736192: #ty >:))
        await ctx.send('*You have plenty of bitches, the furry kind*')
        embed = discord.Embed(
                title="",
                color=discord.Colour.green()
                )
        embed.set_image(url="https://cdn.discordapp.com/attachments/672162533670387855/955686102830817290/7db9dae454c8e4acc4c70d2e0cfe4e5fe3d29d23r1-1200-641v2_hq.png")
        await ctx.send(embed=embed)                                
    else:
        await ctx.send('*Mr. Jingles is unable to call all of your bitches since you have too many.*')
        embed = discord.Embed(
                title="",
                color=discord.Colour.green()
                )
        toomanyurls = ['https://media.makeameme.org/created/too-many-bitches-r3lquk.jpg','https://cdn.discordapp.com/attachments/940395109269254146/955674018596388904/69jbpp.png','https://cdn.discordapp.com/attachments/940395109269254146/955674018596388904/69jbpp.png',
        'https://cdn.discordapp.com/attachments/940395109269254146/955675080652894228/iscLSLtgh13nw5P1nSFDeUlXES7MAAAAASUVORK5CYII.png','https://cdn.discordapp.com/attachments/940395109269254146/955674617060675595/eWRW2ek3he8lgysaireK67ODUVMe55Bf9c3bAOyvocJU601lpxGSErgRpx3EnKrBONXDuuzFFpbfklRmZcOCayYYter4dnEL5OwMlbkvff9IClv9ETJWSAAAAAElFTkSuQmCC.png']
        embed.set_image(url=random.choice(toomanyurls))
        await ctx.send(embed=embed)

#come
@client.command(name='come')
async def come(ctx):
    await ctx.send('*Mr.Jingles looks at you and lays down.*')

#goodnight
@client.command(name='goodnight')
async def goodnight(ctx):
    await ctx.send('*Its time to sleep. Mr.Jingles curls up to your head as he purrs. Your head feels nice and cozy! Mr.Jingles closes his eyes.\nGoodnight Mr Jingles.*')




#BITE
@client.command(name='bite')
async def bite(ctx):

    #if ctx.author.id == 363189216508903424:
        mentionId = ctx.message.mentions[0].id
        if mentionId == 521931888378642443 or mentionId == 96425998089736192:
            await ctx.send('*Mr.Jingles dislikes hairy food.. He refuses to bite<@'+str(mentionId)+'>.*')
        elif mentionId == 676201924642471942:
            await ctx.send('*Mr.Jingles is not in the mood to bite himself today you weirdo.*')
        elif mentionId == 807069645655244820 or mentionId == 606141720563810315:
            await ctx.send('*Mr.Jingles bites <@'+str(mentionId)+'>! He is grateful for the tasty meal!*')
        else:    
            await ctx.send('*Mr.Jingles bites <@'+str(mentionId)+'>! They did not taste very good...*')
    #else:
        #await ctx.send('*Mr.Jingles hisses at you. You do not have any magic salami!*')
    
#pet...
@client.command(name='pet')
async def pet(ctx):
    petOps = ['*Mr.Jingles does a backflip.*','*Mr.Jingles starts purring. Awww*', '*OH NO! Mr.Jingles scratched you.. You are losing a lot of blood... Your vision goes black!! You close your eyes. In your final moments, you think to yourself: it was worth it.*']
    await ctx.send(random.choice(petOps)) 

#talks to the chat
@client.command(name='talk')
async def come(ctx):
    await ctx.send('meow', tts=True)

with open('token.txt', 'r') as file:
    token = file.read().rstrip()
#token
client.run(token)