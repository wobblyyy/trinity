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
import discord
from discord import option
import os



intents = discord.Intents.all()

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('https://x.com'):
        newURL = str(message.content)
        fixedMessageAuthor = str(message.author).split("#")
        newURL = f'{fixedMessageAuthor[0]}: ' + message.content.replace('x.com', 'fixupx.com', 1)
        await message.channel.send(f"{newURL}")

    if message.content.startswith('https://twitter.com'):
        print('success')
        newURL = str(message.content)
        fixedMessageAuthor = str(message.author).split("#")
        newURL = f'{fixedMessageAuthor[0]}: ' + message.content.replace('twitter.com', 'fxtwitter.com', 1)
        await message.channel.send(f"{newURL}")

#
# slash command to fix twitter urls
# replaced by just scanning all messages to see if they start with a twitter url
#
# @bot.slash_command(name="twitterfixer", description="Fixes twitter embeds", guild_ids= [629023030147809282, 1163315129799163974])
# async def twitter_fixer(ctx, twitterurl: discord.Option(discord.SlashCommandOptionType.string)):
#     if 'x.com' in twitterurl:
#         newtext = twitterurl.replace('x.com', 'fixupx.com', 1)
#     elif 'twitter.com' in twitterurl:
#         newtext = twitterurl.replace('twitter.com', 'fxtwitter.com', 1)
#     else:
#         newtext = f'I don\'t know what that url is :('
#     await ctx.respond(f"{newtext}")

#
# cannot figure out how to make ytdlp python api download h264
# so doing it manual
#

@bot.slash_command(name="videodownloader", description="Downloads videos (no tiktok watermarks, either)", guild_ids= [629023030147809282, 1163315129799163974])
async def video_downloads(ctx, videourl: discord.Option(discord.SlashCommandOptionType.string)):

    videourl = videourl.split()
    # remove anyone trying to sneak in a command, I think?
    finalurl = videourl[0]
    video_download = 'yt-dlp -S "+codec:h264" --trim-filename 10 -o "video.%(ext)s" ' + finalurl
    os.system(video_download)
    await ctx.respond(f"Downloading...")
    filename = 'video.mp4'
    if not os.path.exists('video.mp4'):
        await ctx.edit(content=f'Unable to download video as mp4')
    # filesize = os.path.getsize(filename)
    # will use this later to predict if a file will not work
    try:
        await ctx.edit(file=discord.File(filename))
        await ctx.edit(content=f'Done!')
    except:
        await ctx.edit(content=f"Uploading failed :( (File too big?)")
    os.remove(filename) # cleanup!





# ghetto token protection
tokenFile = open('token.txt', 'r')
token = tokenFile.readline()
tokenFile.close()
bot.run(token)

# command just for me?
# @client.command()
# @commands.is_owner()
# async def say(ctx, *, message):
#     await ctx.send(message)
