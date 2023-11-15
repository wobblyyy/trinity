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

bot = discord.Bot(intents=discord.Intents.all())


oppenheimerLinks = ['https://tenor.com/view/oppenheimer-stare-gif-9585562966608025312',
                    'https://tenor.com/view/oppenheimer-starring-then-closing-his-eyes-oppenheimer-oppenheimer-movie-j-robert-oppenheimer-robert-oppenheimer-gif-11256978878629275100',
                    'https://tenor.com/view/oppenheimer-cillian-murphy-movie-scared-horrified-gif-3257036184702814746',
                    'https://tenor.com/view/oppenheimer-cillian-murphy-cillian-murphy-peaky-blinders-gif-1787947313354313976',
                    'https://tenor.com/view/oppenheimer-oppenheimer-movie-walk-walking-gif-3311223081607307352'
                    ]


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

    # well...

    if 'oppenheimer' in message.content.lower():
        await message.channel.send(oppenheimerLinks[random.randint(0, 4)])

    if "male wife" in message.content.lower():
        await message.channel.send(f"my beloved...")

    if bot.user.mentioned_in(message):
        ## if str(message.author) != f'.wabbit#0':
        if message.author.id != 87548407685607424:
            if "love" in message.content.lower():
                await message.channel.send(f"ew...")
            else:
                await message.channel.send(f"sorry, I don't talk to strangers")
        elif "love" in message.content.lower():
            await message.channel.send(f':3')
        else:
            await message.channel.send(f'hello my love')


@bot.slash_command(name="downloadvideo", description="Downloads videos (no tiktok watermarks, either)",
                   guild_ids=[629023030147809282, 1163315129799163974])
async def video_downloads(ctx, videourl: discord.Option(discord.SlashCommandOptionType.string)):
    await ctx.defer()

    videourl = videourl.split()  # remove anyone trying to sneak in a command, I think?
    finalurl = videourl[0]
    print(f'Downloading {finalurl}')
    video_download = 'yt-dlp -S "+codec:h264" -o "video2.%(ext)s" ' + finalurl
    os.system(video_download)
    print(f'Downloaded.')
    filename = glob.glob(os.path.join('video2' + '.*'))[0]
    # filesize = os.path.getsize(filename)
    # will use this later maybe

    try:
        await ctx.send(file=discord.File(filename))
        await ctx.edit(content=f'Done')
    except:
        await ctx.edit(content=f"Uploading failed :( (File too big?)")
        print(f'Something went wrong')
    os.remove(filename)  # cleanup!
    print(f'Finished')




# ghetto token protection
tokenFile = open('token.txt', 'r')
token = tokenFile.readline()
tokenFile.close()
bot.run(token)

