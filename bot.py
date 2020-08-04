import os
import discord
env = open("auth", "r")
TOKEN = env.readline()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content.lower()

    if "me lon" in command:
        await message.channel.send("(me lon)")
        await message.channel.send(file=discord.File('melon.mp4'))

    if "chris" in command:
        await message.channel.send("(chris)")
        await message.channel.send(file=discord.File('Chris.jfif'))

    if "soulja boy" in command:
        await message.channel.send("(soulja boy)")
        await message.channel.send(file=discord.File('Soulja.mov'))

    if command == "what":
        await message.channel.send("(what)")
        await message.channel.send(file=discord.File('what.mp4'))

    if "redfoo" in command:
        await message.channel.send("(redfoo)")
        await message.channel.send(file=discord.File('Redfoo.jpg'))

    if "savage" in command:
        await message.channel.send("(savage)")
        await message.channel.send(file=discord.File('Savage.jpg'))

    if "monke" in command:
        await message.channel.send("(monke)")
        await message.channel.send(file=discord.File('Monke.png'))

    if "pog" in command or "poggers" in command:
        await message.channel.send("(pog)")
        await message.channel.send(file=discord.File('pog.jpg'))

    if "balls" in command:
        await message.channel.send("(balls)")
        await message.channel.send(file=discord.File('Balls.png'))

    if "sunday" in command:
        await message.channel.send("(sunday)")
        await message.channel.send(file=discord.File('Sunday.mp4'))

    if "glizzy" in command or "hotdog" in command or "hot dog" in command:
        await message.channel.send("(glizzy)")
        await message.channel.send(file=discord.File('glizzy.mp4'))


client.run(TOKEN)
