import os
import discord

env = open("auth", "r")
TOKEN = env.readline()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


keywords = ("me lon", "soulja boy", "redfoo", "savage", "monke", "pog", "balls", "sunday", "glizzy",
            "hotdog", "hot dog", "henceforth", "seafood mousse", "pants", "yeah", "mechanic lunch",
            "youngg", "deaduncleben", "everyone", "foot fetish", "ok", "mercy", "imagine dragons", "lol", "lmao",
            "loco ludicolo", "sad", "cry", "depressed", "ed sheeran", "fuck it", "fight club", "covid", "corona",
            "shotgun", "piccolo", "burger king", "nachos", "ferb", "darth maul", "swowss", "italian", "kanye", "allah",
            "chococrispi", "kidney failure", "chef pasqually", "shower", "pizza", "pizza hut", "subway", "lebron james",
            "pepe hands", "lmfao", "shrek", "drake", "shut the fuck up", "onion", "don't care", "dont care", "jaden",
            "ryan", "elaborate", "in conclusion", "you dumb bitch", "tom cruise", "total drama island", "potato",
            "donkey kong", "for real", "what is going on", "league", "felix", "thats awesome", "that's awesome",
            "im done", "i'm done", "racism", "hobby", "ignored", "pee", "grits", "chillin", "brian", "lets go",
            "let's go", "adam", "trex", "beatbox", "beat box", "taric", "beet", "pineapple", "kaden", "gibby",
            "bbq", "the boys", "cow", "butt cheeck", "buttcheeck", "n word", "thug", "sadness", "beans")

res = {"me lon": "memes/melon.mp4", "soulja boy": "memes/Soulja.mov", "redfoo": "memes/Redfoo.jpg", "savage": "memes/Savage.jpg",
       "monke": "memes/Monke.png", "pog": "memes/pog.jpg", "balls": "memes/Balls.png", "sunday": "memes/Sunday.mp4", "glizzy": "memes/glizzy.mp4",
       "hotdog": "memes/glizzy.mp4", "hot dog": "memes/glizzy.mp4", "henceforth": "memes/Henceforth.png", "seafood mousse": "memes/sea.png",
       "pants": "memes/Pants.mp4", "yeah": "memes/Yeah.png", "mechanic lunch": "memes/lunch.jpg", "youngg": "memes/young.jpg",
       "deaduncleben": "memes/young.jpg", "everyone": "memes/everyone.png", "foot fetish": "memes/foot.jpg", "ok": "memes/ok.jpg",
       "mercy": "memes/Mercy.mp4", "imagine dragons": "memes/drag.jpg", "lol": "memes/lmaoi.jpg", "lmao": "memes/lmaoi.jpg", "loco ludicolo": "memes/loco.jpg",
       "sad": "memes/sad.jpg", "cry": "memes/sad.jpg", "depressed": "memes/sad.jpg", "ed sheeran": "memes/ed.jpg", "fuck it": "memes/fit.jpg",
       "fight club": "memes/fight.jpg", "covid": "memes/covid.jpg", "corona": "memes/covid.jpg", "shotgun": "memes/shot.jpg", "piccolo": "memes/burger.mov",
       "burger king": "memes/burger.mov", "nachos": "memes/nachos.jpg", "ferb": "memes/ferb.jpg", "darth maul": "memes/ferb.jpg", "swowss": "memes/swowss.mov",
       "italian": "memes/italian.jpg", "kanye": "memes/kanye.jpg", "allah": "memes/allah.jpg", "chococrispi": "memes/chococrispi.jpg",
       "kidney failure": "memes/kidney.jpg", "chef pasqually": "memes/pasqually.jpg", "shower": "memes/shower.jpg", "pizza": "memes/pizza.mov",
       "pizza hut": "memes/hut.jpg", "subway": "memes/subway.jpg", "lebron james": "memes/james.jpg", "pepe hands": "memes/hands.png", "lmfao": "memes/lmfao.jpg",
       "shrek": "memes/shrek.jpg", "drake": "memes/drake.jpg", "shut the fuck up": "memes/shut.jpg", "onion": "memes/onion.jpg", "don't care": "memes/dont.mov",
       "dont care": "memes/dont.mov", "jaden": "memes/jaden.jpg", "ryan": "memes/ryan.jpg", "elaborate": "memes/elaborate.png",
       "in conclusion": "memes/elaborate.png", "you dumb bitch": "memes/bitch", "tom cruise": "memes/tom.mp4", "total drama island": "memes/island.jpg",
       "potato": "memes/potato.jpg", "donkey kong": "memes/kong.mov", "for real": "memes/real.mov", "what is going on": "memes/going.mp4",
       "league": "memes/league.png", "felix": "memes/felix.png", "thats awesome": "memes/awesome.png", "that's awesome": "memes/awesome.png", "im done": "memes/done.png",
       "i'm done": "memes/done.png", "racism": "memes/racism.png", "hobby": "memes/hobby.jpg", "ignored": "memes/ignored.jpg", "pee": "memes/pee.jpg",
       "grits": "memes/grits.jpg", "chillin": "memes/chillin.jpg", "brian": "memes/chillin.jpg", "lets go": "memes/letsgo.mov", "let's go": "memes/letsgo.mov",
       "adam": "memes/adam.jpg", "trex": "memes/trex.jpg", "beatbox": "memes/beatbox.png", "beat box": "memes/beatbox.png", "taric": "memes/taric.jpg",
       "beet": "memes/beet.jpg", "pineapple": "memes/pineapple.jpg", "kaden": "memes/kaden.jpg", "gibby": "memes/gibby.jpg", "bbq": "memes/bbq.jpg",
       "the boys": "memes/theboys.pnh", "cow": "memes/cow.mov", "butt cheeck": "memes/buttcheeks.mov", "buttcheeck": "memes/buttcheeks.mov", "n word": "memes/nword.png",
       "thug": "memes/thug.jpg", "sadness": "memes/sadness.jpg", "beans": "memes/beans.png"}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content.lower()
    for word in keywords:
        if word in command:
            await message.channel.send("(" + word + ")")
            await message.channel.send(file=discord.File(res[word]))

    if command == "what":
        await message.channel.send("(what)")
        await message.channel.send(file=discord.File('memes/what.mp4'))

    if command == "fuck":
        await message.channel.send("(fuck)")
        await message.channel.send(file=discord.File('memes/fuck.png'))

    if command == "monke words please":
        await message.channel.send(keywords)

client.run(TOKEN)
