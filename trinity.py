#
# Practicing my python with a discord bot
# Incredibly rough around the edges and just as annoying to make as it might be to read
# must have ytdlp installed
#
#
#
#



# https://github.com/Pycord-Development/pycord/releases
# py-cord 2.4.1
#
import os
import glob
import discord
import random



# trinity_egg contains variables for printing
# easter eggs so I can share trinity without spoiling anything ;)

from trinity_egg import *

bot = discord.Bot(intents=discord.Intents.all())



@bot.event
async def on_ready():
    print(f'{bot.user} logged in')




@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith('https://x.com'):
        newURL = message.content.lower()
        fixedMessageAuthor = str(message.author).split("#")
        newURL = f'{fixedMessageAuthor[0]}: ' + newURL.replace('x.com', 'fixupx.com', 1)
        await message.channel.send(f"{newURL}", reference=message)

    if message.content.lower().startswith('https://twitter.com'):
        newURL = message.content.lower()
        fixedMessageAuthor = str(message.author).split("#")
        newURL = f'{fixedMessageAuthor[0]}: ' + newURL.replace('twitter.com', 'fxtwitter.com', 1)
        await message.channel.send(f"{newURL}", reference=message)

    # these eggs could be changed into function calls, probably

    if egg1 in message.content.lower():
        await message.channel.send(egg1Links[random.randint(0, 4)])

    if egg2dot1 in message.content.lower():
        await message.channel.send(egg2dot2)

    if bot.user.mentioned_in(message):
        ## if str(message.author) != f'.wabbit#0':
        if message.author.id != 87548407685607424:
            if egg3dot1 in message.content.lower():
                await message.channel.send(egg3dot2)
            else:
                await message.channel.send(egg3dot3)
        elif egg3dot1 in message.content.lower():
            await message.channel.send(egg3dot4)
        else:
            await message.channel.send(egg3dot5)


@bot.slash_command(name="downloadvideo", description="Downloads videos (no tiktok watermarks, either)",
                   guild_ids=[629023030147809282, 1163315129799163974])
async def video_downloads(ctx, videourl: discord.Option(discord.SlashCommandOptionType.string)):
    await ctx.defer()

    videourl = videourl.split()  # remove anyone trying to sneak in a command, I think?
    finalurl = videourl[0]
    print(f'Downloading {finalurl}')
    video_download = 'yt-dlp -S "+codec:h264" -o "video2.%(ext)s" ' + finalurl
    try:
        os.system(video_download)
        filename = glob.glob(os.path.join('video2' + '.*'))[0]
    except:
        await ctx.edit(content=f'ytdlp failed :(')
    # filesize = os.path.getsize(filename)
    # will use this later maybe
    if os.path.exists(filename):
        print(f'Downloaded.')
        try:
            await ctx.send(file=discord.File(filename))
            await ctx.edit(content=f'Done')
        except:
            await ctx.edit(content=f"Uploading failed :( (File too big?)")
            print(f'Something went wrong')
    else:
        await ctx.edit(content=f'ytdlp failed v2 :( (?)')
    os.remove(filename)  # cleanup!
    print(f'Finished')





# token protection lol
tokenFile = open('token.txt', 'r')
token = tokenFile.readline()
tokenFile.close()
bot.run(token)
