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

    if "henceforth" in command:
        await message.channel.send("(henceforth)")
        await message.channel.send(file=discord.File('Henceforth.png'))

    if "seafood mousse" in command:
        await message.channel.send("(seafood mousse)")
        await message.channel.send(file=discord.File('sea.png'))

    if "pants" in command:
        await message.channel.send("(pants)")
        await message.channel.send(file=discord.File('Pants.mp4'))

    if "yeah" in command:
        await message.channel.send("(yeah)")
        await message.channel.send(file=discord.File('Yeah.png'))

    if "mechanic lunch" in command:
        await message.channel.send("(mechanic lunch)")
        await message.channel.send(file=discord.File('lunch.jpg'))

    if "youngg" in command or "deaduncleben" in command:
        await message.channel.send("(youngG)")
        await message.channel.send(file=discord.File('young.jpg'))

    if "everyone" in command:
        await message.channel.send("(everyone)")
        await message.channel.send(file=discord.File('everyone.png'))

    if "foot fetish" in command:
        await message.channel.send("(foot fetish)")
        await message.channel.send(file=discord.File('foot.jpg'))

    if "ok" in command:
        await message.channel.send("(ok)")
        await message.channel.send(file=discord.File('ok.jpg'))

    if "mercy" in command:
        await message.channel.send("(mercy)")
        await message.channel.send(file=discord.File('Mercy.mp4'))

    if "imagine dragons" in command:
        await message.channel.send("(imagine dragons)")
        await message.channel.send(file=discord.File('drag.jpg'))

    if "lol" in command or "lmao" in command:
        await message.channel.send("(lol)")
        await message.channel.send(file=discord.File('lmaoi.jpg'))

    if "loco ludicolo" in command:
        await message.channel.send("(loco ludicolo)")
        await message.channel.send(file=discord.File('loco.jpg'))

    if "sad" in command or "crying" in command or "cry" in command or "depressed" in command or "depression" in command:
        await message.channel.send("(sad)")
        await message.channel.send(file=discord.File('sad.jpg'))

    if "ed sheeran" in command:
        await message.channel.send("(ed sheeran)")
        await message.channel.send(file=discord.File('ed.jpg'))

    if "fuck it" in command:
        await message.channel.send("(fuck it)")
        await message.channel.send(file=discord.File('fit.jpg'))

    if "fight club" in command:
        await message.channel.send("(fight club)")
        await message.channel.send(file=discord.File('fight.jpg'))

    if "covid" in command or "coronavirus" in command:
        await message.channel.send("(covid)")
        await message.channel.send(file=discord.File('covid.jpg'))

    if "shotgun" in command:
        await message.channel.send("(shotgun)")
        await message.channel.send(file=discord.File('shot.jpg'))

    if "piccolo" in command or "burger king" in command:
        await message.channel.send("(piccolo)")
        await message.channel.send(file=discord.File('burger.jpg'))

    if "nachos" in command:
        await message.channel.send("(nachos)")
        await message.channel.send(file=discord.File('nachos.jpg'))

    if "ferb" in command or "darth maul" in command:
        await message.channel.send("(ferb)")
        await message.channel.send(file=discord.File('ferb.jpg'))

    if "swowss" in command:
        await message.channel.send("(swowss)")
        await message.channel.send(file=discord.File('swowss.mov'))

    if "italian" in command:
        await message.channel.send("(italian)")
        await message.channel.send(file=discord.File('italian.jpg'))

    if "kanye" in command:
        await message.channel.send("(kanye)")
        await message.channel.send(file=discord.File('kanye.jpg'))

    if "allah" in command:
        await message.channel.send("(allah)")
        await message.channel.send(file=discord.File('allah.jpg'))

    if "chococrispi" in command:
        await message.channel.send("(chococrispi)")
        await message.channel.send(file=discord.File('chococrispi.jpg'))

    if "kidney failure" in command:
        await message.channel.send("(kidney failure)")
        await message.channel.send(file=discord.File('kidney.jpg'))

    if "chef pasqually" in command:
        await message.channel.send("(chef pasqually)")
        await message.channel.send(file=discord.File('pasqually.jpg'))

    if "shower" in command:
        await message.channel.send("(shower)")
        await message.channel.send(file=discord.File('shower.jpg'))

    if "pizza" in command:
        await message.channel.send("(pizza)")
        await message.channel.send(file=discord.File('pizza.mov'))

    if "pizza hut" in command:
        await message.channel.send("(pizza hut)")
        await message.channel.send(file=discord.File('hut.jpg'))

    if "subway" in command:
        await message.channel.send("(subway)")
        await message.channel.send(file=discord.File('subway.jpg'))

    if "lebron james" in command:
        await message.channel.send("(lebron james)")
        await message.channel.send(file=discord.File('james.jpg'))

    if "pepe hands" in command:
        await message.channel.send("(pepe hands)")
        await message.channel.send(file=discord.File('hands.png'))

    if "lmfao" in command:
        await message.channel.send("(lmfao)")
        await message.channel.send(file=discord.File('lmfao.jpg'))

    if "shrek" in command:
        await message.channel.send("(shrek)")
        await message.channel.send(file=discord.File('shrek.jpg'))
client.run(TOKEN)
