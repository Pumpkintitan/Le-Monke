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
        await message.channel.send(file=discord.File('memes/melon.mp4'))

    if "chris" in command:
        await message.channel.send("(chris)")
        await message.channel.send(file=discord.File('memes/Chris.jfif'))

    if "soulja boy" in command:
        await message.channel.send("(soulja boy)")
        await message.channel.send(file=discord.File('memes/Soulja.mov'))

    if command == "what":
        await message.channel.send("(what)")
        await message.channel.send(file=discord.File('memes/what.mp4'))

    if "redfoo" in command:
        await message.channel.send("(redfoo)")
        await message.channel.send(file=discord.File('memes/Redfoo.jpg'))

    if "savage" in command:
        await message.channel.send("(savage)")
        await message.channel.send(file=discord.File('memes/Savage.jpg'))

    if "monke" in command:
        await message.channel.send("(monke)")
        await message.channel.send(file=discord.File('memes/Monke.png'))

    if "pog" in command or "poggers" in command:
        await message.channel.send("(pog)")
        await message.channel.send(file=discord.File('memes/pog.jpg'))

    if "balls" in command:
        await message.channel.send("(balls)")
        await message.channel.send(file=discord.File('memes/Balls.png'))

    if "sunday" in command:
        await message.channel.send("(sunday)")
        await message.channel.send(file=discord.File('memes/Sunday.mp4'))

    if "glizzy" in command or "hotdog" in command or "hot dog" in command:
        await message.channel.send("(glizzy)")
        await message.channel.send(file=discord.File('memes/glizzy.mp4'))

    if "henceforth" in command:
        await message.channel.send("(henceforth)")
        await message.channel.send(file=discord.File('memes/Henceforth.png'))

    if "seafood mousse" in command:
        await message.channel.send("(seafood mousse)")
        await message.channel.send(file=discord.File('memes/sea.png'))

    if "pants" in command:
        await message.channel.send("(pants)")
        await message.channel.send(file=discord.File('memes/Pants.mp4'))

    if "yeah" in command:
        await message.channel.send("(yeah)")
        await message.channel.send(file=discord.File('memes/Yeah.png'))

    if "mechanic lunch" in command:
        await message.channel.send("(mechanic lunch)")
        await message.channel.send(file=discord.File('memes/lunch.jpg'))

    if "youngg" in command or "deaduncleben" in command:
        await message.channel.send("(youngG)")
        await message.channel.send(file=discord.File('memes/young.jpg'))

    if "everyone" in command:
        await message.channel.send("(everyone)")
        await message.channel.send(file=discord.File('memes/everyone.png'))

    if "foot fetish" in command:
        await message.channel.send("(foot fetish)")
        await message.channel.send(file=discord.File('memes/foot.jpg'))

    if "ok" in command:
        await message.channel.send("(ok)")
        await message.channel.send(file=discord.File('memes/ok.jpg'))

    if "mercy" in command:
        await message.channel.send("(mercy)")
        await message.channel.send(file=discord.File('memes/Mercy.mp4'))

    if "imagine dragons" in command:
        await message.channel.send("(imagine dragons)")
        await message.channel.send(file=discord.File('memes/drag.jpg'))

    if "lol" in command or "lmao" in command:
        await message.channel.send("(lol)")
        await message.channel.send(file=discord.File('memes/lmaoi.jpg'))

    if "loco ludicolo" in command:
        await message.channel.send("(loco ludicolo)")
        await message.channel.send(file=discord.File('memes/loco.jpg'))

    if "sad" in command or "crying" in command or "cry" in command or "depressed" in command or "depression" in command:
        await message.channel.send("(sad)")
        await message.channel.send(file=discord.File('memes/sad.jpg'))

    if "ed sheeran" in command:
        await message.channel.send("(ed sheeran)")
        await message.channel.send(file=discord.File('memes/ed.jpg'))

    if "fuck it" in command:
        await message.channel.send("(fuck it)")
        await message.channel.send(file=discord.File('memes/fit.jpg'))

    if "fight club" in command:
        await message.channel.send("(fight club)")
        await message.channel.send(file=discord.File('memes/fight.jpg'))

    if "covid" in command or "coronavirus" in command:
        await message.channel.send("(covid)")
        await message.channel.send(file=discord.File('memes/covid.jpg'))

    if "shotgun" in command:
        await message.channel.send("(shotgun)")
        await message.channel.send(file=discord.File('memes/shot.jpg'))

    if "piccolo" in command or "burger king" in command:
        await message.channel.send("(piccolo)")
        await message.channel.send(file=discord.File('memes/burger.jpg'))

    if "nachos" in command:
        await message.channel.send("(nachos)")
        await message.channel.send(file=discord.File('memes/nachos.jpg'))

    if "ferb" in command or "darth maul" in command:
        await message.channel.send("(ferb)")
        await message.channel.send(file=discord.File('memes/ferb.jpg'))

    if "swowss" in command:
        await message.channel.send("(swowss)")
        await message.channel.send(file=discord.File('memes/swowss.mov'))

    if "italian" in command:
        await message.channel.send("(italian)")
        await message.channel.send(file=discord.File('memes/italian.jpg'))

    if "kanye" in command:
        await message.channel.send("(kanye)")
        await message.channel.send(file=discord.File('memes/kanye.jpg'))

    if "allah" in command:
        await message.channel.send("(allah)")
        await message.channel.send(file=discord.File('memes/allah.jpg'))

    if "chococrispi" in command:
        await message.channel.send("(chococrispi)")
        await message.channel.send(file=discord.File('memes/chococrispi.jpg'))

    if "kidney failure" in command:
        await message.channel.send("(kidney failure)")
        await message.channel.send(file=discord.File('memes/kidney.jpg'))

    if "chef pasqually" in command:
        await message.channel.send("(chef pasqually)")
        await message.channel.send(file=discord.File('memes/pasqually.jpg'))

    if "shower" in command:
        await message.channel.send("(shower)")
        await message.channel.send(file=discord.File('memes/shower.jpg'))

    if "pizza" in command:
        await message.channel.send("(pizza)")
        await message.channel.send(file=discord.File('memes/pizza.mov'))

    if "pizza hut" in command:
        await message.channel.send("(pizza hut)")
        await message.channel.send(file=discord.File('memes/hut.jpg'))

    if "subway" in command:
        await message.channel.send("(subway)")
        await message.channel.send(file=discord.File('memes/subway.jpg'))

    if "lebron james" in command:
        await message.channel.send("(lebron james)")
        await message.channel.send(file=discord.File('memes/james.jpg'))

    if "pepe hands" in command:
        await message.channel.send("(pepe hands)")
        await message.channel.send(file=discord.File('memes/hands.png'))

    if "lmfao" in command:
        await message.channel.send("(lmfao)")
        await message.channel.send(file=discord.File('memes/lmfao.jpg'))

    if "shrek" in command:
        await message.channel.send("(shrek)")
        await message.channel.send(file=discord.File('memes/shrek.jpg'))

    if "drake" in command:
        await message.channel.send("(drake)")
        await message.channel.send(file=discord.File('memes/drake.jpg'))

    if "shut the fuck up" in command:
        await message.channel.send("(shut the fuck up)")
        await message.channel.send(file=discord.File('memes/shut.jpg'))

    if "onion" in command:
        await message.channel.send("(onion)")
        await message.channel.send(file=discord.File('memes/onion.jpg'))

    if "don't care" in command or "dont care" in command:
        await message.channel.send("(don't care)")
        await message.channel.send(file=discord.File('memes/dont.mov'))

    if "fuck" in command:
        await message.channel.send("(fuck)")
        await message.channel.send(file=discord.File('memes/fuck.png'))

    if "jaden" in command:
        await message.channel.send("(jaden)")
        await message.channel.send(file=discord.File('memes/jaden.jpg'))

    if "ryan" in command:
        await message.channel.send("(ryan)")
        await message.channel.send(file=discord.File('memes/ryan.jpg'))
client.run(TOKEN)
