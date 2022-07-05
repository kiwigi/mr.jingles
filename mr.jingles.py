tofuzu
#0001

🌸 mar 🌸 — 01/15/2022
https://cloud.tylerchen.ca/index.php/s/TrDb24QR7CTryR6
VividEradicator
Mar sus behaviour.mp4
VividEradicator - VividEradicator's Server
🌸 mar 🌸 — 01/19/2022
Image
Image
🌸 mar 🌸 — 01/20/2022
Image
Image
🌸 mar 🌸 — 01/21/2022
Image
Image
Image
Image
🌸 mar 🌸 — 01/22/2022
Image
Image
🌸 mar 🌸 — 01/24/2022
Image
🌸 mar 🌸 — 01/24/2022
Image
Image
🌸 mar 🌸 — 01/24/2022
Image
Image
Image
Image
Image
🌸 mar 🌸 — 01/25/2022
Attachment file type: document
asd_verification.doc
1.05 MB
🌸 mar 🌸 — 01/25/2022
Attachment file type: acrobat
asd_verification.pdf
11.03 MB
🌸 mar 🌸 — 01/25/2022
Image
🌸 mar 🌸 — 01/27/2022
Image
🌸 mar 🌸 — 01/27/2022
Image
🌸 mar 🌸 — 01/27/2022
Image
Image
Image
Image
🌸 mar 🌸 — 01/27/2022
Image
🌸 mar 🌸 — 01/27/2022
🌸 mar 🌸 — 01/28/2022
Image
Image
Image
Image
Image
Image
Attachment file type: unknown
cat.psd
785.67 KB
🌸 mar 🌸 — 02/02/2022
Image
🌸 mar 🌸 — 02/02/2022
Image
Image
Image
Image
🌸 mar 🌸 — 02/06/2022
https://playvalorant.com/en-us/media/?linkId=100000107930620
VALORANT: Riot Games’ competitive 5v5 character-based tactical shoo...
Riot Games presents VALORANT: a 5v5 character-based tactical FPS where precise gunplay meets unique agent abilities. Learn about VALORANT and its stylish cast
VALORANT: Riot Games’ competitive 5v5 character-based tactical shoo...
🌸 mar 🌸 — 02/10/2022
Image
Image
Image
🌸 mar 🌸 — 02/14/2022
https://youtu.be/EGd2H11qKPI
YouTube
발로란트
Can't Slow Me Down // 미란이(Mirani), 릴보이(lIlBOI), GroovyRoom // 제트 뮤직...
Image
🌸 mar 🌸 — 02/16/2022
Attachment file type: document
TMA1.docx
41.41 KB
🌸 mar 🌸 — 02/18/2022
Attachment file type: unknown
Haze_Long_Portrait_Brushes.brushset
5.46 MB
Attachment file type: unknown
Easy_Skin_Tone_.swatches
1.09 KB
Attachment file type: unknown
Haze_Long__.brushset
6.12 MB
🌸 mar 🌸 — 02/18/2022
Attachment file type: unknown
Haze_Long_Sketch_Brush_Variants_.brushset
399.70 KB
Attachment file type: unknown
Brushwork_Practice_Sheets.procreate
61.02 MB
🌸 mar 🌸 — 02/18/2022
Image
🌸 mar 🌸 — 02/19/2022
Image
🌸 mar 🌸 — 02/21/2022
Image
🌸 mar 🌸 — 02/23/2022
Image
Image
🌸 mar 🌸 — 03/03/2022
🌸 mar 🌸 — 03/03/2022
https://ecologylab.net/courses/hcc/hostedMaterials/curtisVertelneyChi90Storyboards.pdf
🌸 mar 🌸 — 03/09/2022
Image
🌸 mar 🌸 — 05/10/2022
Attachment file type: acrobat
Online_Return_Center.pdf
109.19 KB
🌸 mar 🌸 — 05/21/2022
Image
Image
Attachment file type: unknown
MG_0644.CR2
33.44 MB
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
Image
tofuxu — Today at 4:44 AM
I,
Image
🌸 mar 🌸 — Today at 9:22 PM
#Mr.Jingles is your friend

import discord
from discord.ext import commands
import random
import time
Expand
message.txt
10 KB
﻿
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
@client.command(name='talk')
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
    elif ctx.author.id == 324680839084507149: #gagan
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
async def come(ctx):
    await ctx.send('*Its time to sleep. Mr.Jingles curls up to your head as he purrs. Your head feels nice and cozy! Mr.Jingles closes his eyes.\nGoodnight Mr Jingles.*')

#feed menu and options
@client.command(name='feed')
async def feed(ctx):
    #await ctx.send('What would you like to feed Mr.Jingles?')
    await ctx.send('Whats on the menu??\nsalami: feed salami\ntuna: feed tuna\nvegtabl: feed vegtabl\nloops: feed Frootloops™')
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
            elif message.content== 'feed loops':
                await ctx.send('*Mr.Jingles feeds on the loops...*')
                m=await ctx.send("MEOW!!!!")
                await ctx.send(content="Translation: Thank you for the lööps, brøther.")
                await client.process_commands(message)
            else:
                #await ctx.send("*that wasn't an option dummy*")
                await client.process_commands(message)
    await client.process_commands(message)


#BITE
@client.command(name='bite')
async def bite(ctx):

    #if ctx.author.id == 363189216508903424:
        mentionId = ctx.message.mentions[0].id
        if mentionId == 521931888378642443 or mentionId == 96425998089736192:
            await ctx.send('*Mr.Jingles dislikes hairy food.. He refuses to bite<@'+str(mentionId)+'>.*')
        elif mentionId == 676201924642471942:
            await ctx.send('*Mr.Jingles is not in the mood to bite himself today you weirdo.*')
        elif mentionId == 324680839084507149 or mentionId == 606141720563810315:
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

#talks to the chat - go to bed!
@client.command(name='gotobed')
async def come(ctx):
    await ctx.send('ITS PAST YOUR BEDTIME', tts=True)


#token
client.run('token')