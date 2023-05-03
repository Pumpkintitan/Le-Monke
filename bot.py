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
            "everyone", "foot fetish", "ok", "mercy", "imagine dragons", "lol", "lmao",
            "sad", "cry", "depressed", "ed sheeran", "fuck it", "fight club",
            "shotgun", "piccolo", "burger king", "nachos", "ferb", "darth maul", "swowss", "italian", "kanye", "allah",
            "chococrispi", "kidney failure", "chef pasqually", "shower", "pizza", "pizza hut", "subway", "lebron james",
            "pepe hands", "lmfao", "shrek", "drake", "shut the fuck up", "onion", "don't care", "dont care", "jaden",
            "ryan", "elaborate", "in conclusion", "you dumb bitch", "tom cruise", "total drama island", "potato",
            "donkey kong", "for real", "what is going on", "league", "thats awesome", "that's awesome",
            "im done", "i'm done", "racism", "hobby", "ignored", "pee", "grits", "chillin", "brian", "lets go",
            "let's go", "adam", "trex", "beet", "pineapple", "kaden", "gibby",
            "bbq", "butt cheeck", "buttcheeck", "n word", "thug", "beans", "agony", "crack",
            "subway foot", "meow", "suffering", "poop", "emperor tamarin", "movie theater", "imposter", "popare", "wolf order",
            "the guys", "for africa", "3/24/1979", "gorilla joke", "7018 rod", "hercules plates", "yo dudes", "drill sargeant",
            "people", "cheeze-it flakes", "cheese it flakes", "peanut butter and onion sandwich", "spotify", "making burger",
            "wocky slush", "albania", "bread", "chicken sandwich", "cyborg", "dj khaled", "doctor examining my balls", 
            "freshest cut", "goji", "hog rider", "karate", "mc griddle", "movie food", "no bitches", "old woman bread", 
            "orn free taa", "pie", "red faced uakari", "scooby doo", "silly circles", "vaping memes", "wave check", 
            "weed", "wingstop", "yo grandma", "wheat grain funny stock image", "nicky flippers", "mom")
printwords = "```"
for word in keywords:
    printwords += (word + ", ")
printwords += "pi```"

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
       "in conclusion": "memes/elaborate.png", "you dumb bitch": "memes/bitch.png", "tom cruise": "memes/tom.mp4", "total drama island": "memes/island.jpg",
       "potato": "memes/potato.jpg", "donkey kong": "memes/kong.mov", "for real": "memes/real.mov", "what is going on": "memes/going.mp4",
       "league": "memes/league.png", "felix": "memes/felix.png", "thats awesome": "memes/awesome.png", "that's awesome": "memes/awesome.png", "im done": "memes/done.png",
       "i'm done": "memes/done.png", "racism": "memes/racism.png", "hobby": "memes/hobby.jpg", "ignored": "memes/ignored.jpg", "pee": "memes/pee.jpg",
       "grits": "memes/grits.jpg", "chillin": "memes/chillin.jpg", "brian": "memes/brian.png", "lets go": "memes/letsgo.mov", "let's go": "memes/letsgo.mov",
       "adam": "memes/adam.jpg", "trex": "memes/trex.jpg", "beatbox": "memes/beatbox.png", "beat box": "memes/beatbox.png", "taric": "memes/taric.jpg",
       "beet": "memes/beet.jpg", "pineapple": "memes/pineapple.jpg", "kaden": "memes/kaden.jpg", "gibby": "memes/gibby.jpg", "bbq": "memes/bbq.jpg",
       "the boys": "memes/theboys.png", "cow": "memes/cow.mov", "butt cheeck": "memes/buttcheeks.mov", "buttcheeck": "memes/buttcheeks.mov", "n word": "memes/nword.png",
       "thug": "memes/thug.jpg", "sadness": "memes/sadness.jpg", "beans": "memes/beans.png", "agony": "memes/agony.jpg", "crack": "memes/crack.png",
       "subway foot": "memes/subfoot.jpg", "meow": "memes/meow.jpg", "suffering": "memes/suffering.png", "poop": "memes/poop.mp4", "emperor tamarin": "memes/tamarin.jpg",
       "movie theater": "memes/movie.png", "imposter": "memes/imposter.png", "popare": "memes/popare.png", "wolf order": "memes/wolf.png", "the guys": "memes/guys.png",
       "for africa": "memes/africa.png", "3/24/1979": "memes/1979.mov", "gorilla joke": "memes/gorilla.png", "7018 rod": "memes/7018.jpg", "hercules plates": "memes/hercules.png",
       "yo dudes": "memes/dudes.mov", "drill sargeant": "memes/sargeant.png", "people": "memes/people.jpg", "cheeze-it flakes": "memes/flakes.png",
       "cheese it flakes": "memes/flakes.png", "peanut butter and onion sandwich": "memes/PBaO.jpg", "spotify": "memes/spotify.jpg", "making burger": "memes/mburger.mov",
       "wocky slush": "memes/wocky.mp4", "albania": "memes/albania.jpg", "bread": "memes/bread.jpg", "chicken sandwich": "memes/chickensand.jpg", "cyborg": "memes/cyborg.jpg", "dj khaled": "memes/djkhaled.jpg",
        "doctor examining my balls": "memes/doctor.jpg", "freshest cut": "memes/fresh.jpg", "goji": "memes/goji.jpg", "hog rider": "memes/hogrider.jpg", "karate": "memes/karate.jpg", 
        "mc griddle": "memes/mcgriddle.jpg", "movie food": "memes/moviefood.jpg", "no bitches": "memes/nobitches.jpg", "old woman bread": "memes/oldwomanbread.jpg", "orn free taa": "memes/ornfreetaa.jpg", 
        "pie": "memes/pie.jpg", "red faced uakari": "memes/redfaced.jpg", "scooby doo": "memes/scoob.jpg","silly circles": "memes/sillycircles.jpg", "vaping memes": "memes/vapingmemes.jpg", "wave check": "memes/wavecheck.jpg", 
        "weed": "memes/weed.jpg", "wingstop": "memes/wingstop.jpg", "yo grandma": "memes/yograndma.jpg", "wheat grain funny stock image": "memes/wheat.jpg", "nicky flippers": "memes/nicky.mov",
        "mom": "memes/mom.PNG"}


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
        await message.channel.send(printwords)
        
    if "pi" in command:
        await message.channel.send("(pi)")
        await message.channel.send("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590")

client.run(TOKEN)
