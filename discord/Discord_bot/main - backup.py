import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import random as fuck
import os
import cogs
from itertools import cycle
import youtube_dl
from async_timeout import timeout
import requests
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
import datetime
import asyncio
import ffmpeg

client = commands.Bot(command_prefix = 'st!')

for filename in os.listdir('./data'):
    if filename.endswith('.py'):
        client.load_extension(f'data.{filename[:-3]}')

bullshit = ["Your day might have not been the best, but atleast there will always be tommorow.","Today is not your day isn't it","My condolences",
"Are you feeling down? It's always better to not think much about what transpired.","Get some rest","A mere breeze before the storm it was, prepare to face hardship even worse than your last",
"I suppose thinking more positively may help with your problem","I don't want to tell you.","I never see the future but I can assure you that you will acomplish something soon.","Greater than swords is the determination of its holder, You can do it!",
"Rest assured, there is little to be worried about."

]

stat = ['Trying to find love',
'Persuing love',
'Idolizing someone',
'Cheering for you',
'Loving Monika',
'Hyperdimension Neptunia',
'Initiating destruction sequence',
'Loving myself',
'He will not escape',
'version 27.12'
]




@client.event
async def on_ready():

    global stat
    fuck.seed()
    rand = fuck.choice(stat)
    await client.change_presence(status=discord.Status.idle,activity = discord.Game(rand))
    print('I exists.')

    client.unload_extension(f'data.DNOP')
    define.start()
    #   #jump



@client.event
async def on_member_join(member):
    print(f'{member} has joined.')
@client.event
async def on_member_leave(member):
    print(f'Detected the departure of {member}')



@client.command(aliases = ['tell','converse','convey'],pass_context=True)
async def say(ctx, *, question):
    response = question
    await ctx.send(question)
    await client.delete_message(message)

@client.command(pass_context=True)
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"Removed {amount} messages.")

@clear.error
async def clear_error(error, ctx):
    if isinstance(error , CheckFailure):
        await ctx.send("What are you trying to acomplish?")


@client.command()
async def ping(ctx):

    late = round(client.latency * 1000)
    if late > 100:
        await ctx.send(f'{late}ms, Holy shit you live in the moutains or somethin?')

    if late < 100:
        await ctx.send(f"{late}ms")


@client.command(aliases = ['hb','HB'])
async def honsballs(ctx, *, question):

    if "69" in question or "Nont" in question:
        await ctx.send(f"You have typed: **{question}**\nMy answer: Don't ask me about these stuffs")

    elif len(question) < 7:
        await ctx.send(f"You have typed: **{question}**\nMy answer: I don't think that's a question")

    else:
        answers = ['No','Never possible','Definitely not','Impossible','Possibly so','I suppose you might be correct','I think you are correct','That is wrong, trust me','Go ask Nont','Most Tight.','Correct.','Bitch dont ask me this shit','I am not sure','Your question held too much value for my simple brain to process']
        newseed = str(question).lower()+"HB" +str(ctx.message.author.id)
        fuck.seed(newseed)
        await ctx.send(f'You have typed: **{question}**\nMy answer: **{fuck.choice(answers)}**')

@client.command(aliases = ['21'])
async def twentyoneballs(ctx, *, question):
        answers = ['No.','Never possible','Definitely not','Inevitable','Possibly so','I suppose you might be correct','I think you are correct','That is wrong, trust me','Go ask Nont','I can not answer.','Correct.','Bitch dont ask me this shit','I am not sure','Your question held too much value for my simple brain to process','Yes','Without a doubt','There is a possibility','Clearly so','It will be slowly but surely.']
        newseed = str(question).lower()+"hakke" +str(ctx.message.author.id)
        fuck.seed(newseed)
        await ctx.send(f'You have typed: **{question}**\nMy answer: **{fuck.choice(answers)}**')

@client.command(aliases = ['Jesus'])
async def pick(ctx, *,question):
    listeee = question.split(" or ")
    newseed = str(question).lower()+"Jesus" +str(ctx.message.author.id)
    fuck.seed(newseed)
    await ctx.send(f"You have typed: **{question}**\nI would pick: **{listeee[fuck.randint(0, 1)]}**")

@client.command()
async def ship(ctx, *,question):
    listeee = question.split(" and ")
    newseed =  str(question).lower() + "Venus"
    fuck.seed(newseed)
    randoms = fuck.randint(0, 100)

    await ctx.send(f"I suppose {question}'s compatability would be \n**{randoms}%**")
    if random == 100:
        await ctx.send("What a luck!")
    elif randoms > 80:
        await ctx.send("I think it would go well!")
    elif random > 50:
        await ctx.send("Could go either way I guess?")
    elif random > 10:
        await ctx.send("Might not go well?")
    elif random > 0:
        await ctx.send("My condolences")
    else:
        await ctx.send("....")

@client.command()
async def echo(ctx, * ,relm):
    await ctx.send(relm)

@client.command()
async def true_echo(ctx, *,relm):
    await ctx.send(f"``{relm}``")



@client.command()
#@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def sudo(ctx, sudo ,name):

    voidstring = name
    voidstring = voidstring.replace(">","")
    voidstring = voidstring.replace("<","")
    voidstring = voidstring.replace("@","")
    voidstring = voidstring.replace("!","")

    if sudo == "cunt":
        listeeee = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World", "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups", "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"]
        dated = datetime.date.today()


        nseed = str(voidstring) + "visanu" + str(dated)
        fuck.seed(nseed)
        beyond = str(fuck.choice(listeeee))
        reversed = fuck.randint(0,1)

        if reversed == 0:
            await ctx.send(f"{name}'s card of the day is **{beyond}**")
        else:
            await ctx.send(f"{name}'s card of the day is **{beyond}** reversed")

    if sudo == "getid":
        await ctx.send(ctx.message.mentions[0].id)

    if sudo == "":
        await ctx.send("Void detected?")

    if sudo == "":
        print("wat")

    if sudo == "fortune":
        dated = datetime.date.today()
        nseed = str(voidstring) + "Zeus" + str(dated)
        fuck.seed(nseed)
        global bullshit
        resultant = str(fuck.choice(bullshit))
        await ctx.send(resultant)

    if sudo == "admin" and name == "69":
        if ctx.message.author.id == 307448724089733120:
            manual.start()
        else:
            await ctx.send("Don't bother trying what you can't do.")
#jump


nc = ["Expedition","1st Kingdom","2nd Storm","3rd War","4th Calling","5th Empire","6th Collaspe","7th Attempt","8th Hero","9th Sword","10th Empress","11th Mirrors","12th Sin","13th Truth",
"Journal", "I Inside" , "II Behind" , "III Hall" , "IV Cathedral" , "V Messenger" , "VI Serenity" , "VII Finale" , "VIII Showdown" , "IX Senses" , "X Numb" , "XI Beyond" , "XII Barrier" , "XIII Sentiment",
"The Ender"
]

meanings = {
"Expedition" : "The court calls for 10 adventures, To go out and seek out ruins, To find evidences of the First Kingdom.",
"1st Kingdom" : "A long way we marched, The ruins are on the horizon. In deepest part of the forest we saw, The ruins of the First Kingdom.",
"2nd Storm" : "Together we gathered, Exploration we did. Unknown we sits, Amidst the storm.",
"3rd War" : "In our escape, From the great tempest. Before we rest, We heard the horns.",
"4th Calling" : "Home we went, Our swords plagued with dents. Yet another calling we get. Have they loses all their senses?",
"5th Empire" : "The cries of war was heard. The Empire made its move. Though pointless it was. We stand before them.",
"6th Collaspe" : "The realization came true, As we saw the true horror of war. Nothing could be on par, With corpses of your friends.",
"7th Attempt" : "The commanders has fled. With a thread of hope gone, We call for final attempt.",
"8th Hero" : "In novels and lies, One would rise and put all evil to demise. Though as harsh as it may be. There is no hero.",
"9th Sword" : "My blade still aches from the storm, My sight still blurred from fires and corpses. A man stand before me, I gripped my broken sword and strike at him.",
"10th Empress" : "Before me was a beauty, I don't remember a thing. But one thing I know, is that she saved me.",
"11th Mirrors" : "Days has passed, The bloodsheds still lingered on my mind, I can't get their faces out of my head. Just then she came to comfort me.",
"12th Sin" : "Though it may be a great sin, Though it may be ungrateful. I could not resist. I will break in her room.",
"13th Truth" : "In the middle of the night, I sneaked in to her room. I could not find her, But a chill went down my spine. Who knows that a single piece of paper will end it all.",

"Journal" : "O how the time flies days to days. I grabbed my rusted crown and take a walk down the ruined hallway.",
"I Inside" : "Inside the deep dark hall there lies a countless lifeless bodies once guard the palace.",
"II Behind" : "I steps further into the darkness only to be greeted with something that's behind me",
"III Hall" : "In the depths of the halls, the haunted,lingering,echoing voices of the fallen soilders and citizen dominates my mind and thoughts. The guilt is real.",
"IV Cathedral" : "In the middle of the ruined kingdom there lies an unbreaking cathedral. It somehow survived the test of both war and time."
}







@client.command()
async def cunt2(ctx):
    global nc
    global meaning

    dated = datetime.date.today()
    ndated = str(dated) + "sayo"

    fuck.seed(dated)
    beyond = str(fuck.choice(nc))
    reversed = fuck.randint(0,1)

    if reversed == 0:
        try:
            await ctx.send(f"**{beyond}** was drawn \n{meanings[beyond]}")
        except Exception as c:
            await ctx.send(f"**{beyond}** was drawn \nDescription undetected\n\nException occured:\n{c}")

    else:
        try:
            beyond = str(beyond) + " reversed"
            await ctx.send(f"**{beyond}** was drawn \n{meanings[beyond]}")
        except Exception as c:
            await ctx.send(f"**{beyond}** was drawn \nDescription undetected\n\nException occured:\n{c}")


@client.command()
async def draw2(ctx,* ,amount):
    global nc

    fuck.seed()
    amount = int(amount)
    drawn = fuck.sample(nc,amount)
    voi = ""
    c = len(drawn)
    c -= 1

    if amount == 0:
        await ctx.send("What are you trying to acomplish")
    if amount == 1:
        await ctx.send(f"**{drawn[0]}** has been drawn")
    else:
        for temporal in drawn:
            if temporal == drawn[c]:
                check = fuck.randint(0,1)
                if  check == 0:
                    check = "(Reversed)"
                else:
                    check = ""
                voi += f"and {temporal}{ check}."
                break
            else:
                check = fuck.randint(0,1)
                if  check == 0:
                    check = "(Reversed)"
                else:
                    check = ""

                voi += temporal
                voi += check
                voi += " ,  "

        await ctx.send(f"I have drawn:    **{voi}**")




#jump#j


@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command(aliases = ['dis'])
async def disconnect(ctx):
    await ctx.voice_client.disconnect()




listeeee = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World", "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups", "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"]



tarotdeck = {
 "The Fool":  "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel." , "rdesc" : "Folly, failure, madness. Hindered travel." ,
 "The Magician":  "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends." , "rdesc" : "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery." ,
 "The High Priestess":  "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way." , "rdesc" : "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality." ,
 "The Empress": "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development." , "rdesc" : "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending." ,

 "The Emperor":  "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person." , "rdesc" : "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac." ,
 "The Hierophant": "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers." , "rdesc" : "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently." ,
 "The Lovers": "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life." , "rdesc" : "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation." ,
 "The Chariot": "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel." , "rdesc" : "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente." ,
 "Strength": "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust." , "rdesc" : "Discord, ruin, stubbornness, abuse of power. Weakness." ,
 "The Hermit": "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development." , "rdesc" : "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies." ,
 "The Wheel of Fortune": "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions." , "rdesc" : "Retarded progress. Delays, setbacks." ,
 "Justice": "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation." , "rdesc" : "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance." ,
 "The Hanged Man":  "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation." , "rdesc" : "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure." ,
 "Death":  "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another." , "rdesc" : "Stagnation, death, petrification. Incurable ill person. Broken marriage." ,
 "Temperance":  "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will." , "rdesc" : "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck." ,
 "The Devil": "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out." , "rdesc" : "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth." ,
 "The Blasted Tower": "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death." , "rdesc" : "Complete confusion. The gain of freedom at great cost. False accusations, oppression." ,
 "The Star": "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health." , "rdesc" : "Arrogance, pessimism, stubbornness. Illness. Error of judgment." ,
 "The Moon": "Intuition, threshold of an important change, arduous and obscure path, development of psychic powers." , "rdesc" : "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer." ,
 "The Sun":  "Glory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others." , "rdesc" : "Anoyances, disguise. Arrogance. Broken engagement or lost job." ,
 "Judgement":  "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor." , "rdesc" : "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment." ,
 "The World": "Success granted. Rewards. Travel, emigration, change of residence." , "rdesc" : "Hindrances, stagnation. Hard work to bring success." ,
 "King of Wands": "Courageous, swift and generous man. Passionate and strong. Paternalistic and proud. May be a country gentleman, generally married. Unexpected heritage; a good marriage." , "rdesc" : "Despotic, bigoted, prejudiced, evil-minded." ,
 "Queen of Wands":  "Kind, energetic but calm woman. Conservative, pragmatic and authoritarian. Fruitful in mind and body." , "rdesc" : "Domineering, jealous, dogmatic and irrational. Quick to take offense." ,
 "Knight of Wands": "A young and energetic man. Swift and daring. May be noble and generous but also violent and hasty." , "rdesc" : "Jealous, weak and intolerant person. Quarrel, discord, frustration." ,
"Page of Wands":  "Young and brilliant. Enthusiastic and daring. A messenger or bearer of tidings." , "rdesc" : "Frivolous youth. Theatrical and shallow. Cruel, oppressive." ,
"Ace of Wands": "Creation, birth. The power or ability to begin or to follow through energetically with a plan or task; enterprise and determination. Beginning of an enterprise, invention or adventure." , "rdesc" : "Fall. To lose or postpone something (employment, enterprise, etc.). False starts." ,
"Two of Wands":  "Dominion. Maturity. Boldness with self-control. Influence." , "rdesc" : "Disturbance. Indifferent to or disregardful of consequences. Fear, illness." ,
"Three of Wands":   "Virtue. Established strength, realization of hope, nobility. Cooperation, partnership." , "rdesc" : "Inconsistency, deception, treachery. Loss, robbery." ,
"Four of Wands":  "Completion. Settlement, peace, harmony. Romance, marriage, society." , "rdesc" : "Insecurity. Uneasiness, unreliableness. Contradictions, incomplete happiness." ,
"Five of Wands":  "Strife. Competition, lawsuit, obstacles, violence, fighting." , "rdesc" : "Dangerous indecision, treachery, complication." ,
"Six of Wands":  "Victory after strife. Good news. Progress, helping friends." , "rdesc" : "Postponement. Insolence, excessive pride. Treason." ,
"Seven of Wands":   "Valor. Victory through courage. Struggle. Fierce competition. Certain success." , "rdesc" : "Uncertainty and fear. Pregnancy. False appearance." ,
"Eight of Wands":   "Swiftness. Hasty decision. Air travel, messages. Love letter. Hyperactivity. Great hopes." , "rdesc" : "Opposition. Jealousness. Delay in business or love affair." ,
"Nine of Wands":   "Strength. Capability of enduring a long struggle and achieve the final victory. Recovery from sickness." , "rdesc" : "Weakness, delays, sickness. Adversity." ,
"Ten of Wands":  "Oppression. Imbalance and selfishness. Heavy burden. Force detached from spiritual sources. A problem may be solved soon." , "rdesc" : "Annoyances. Treason. Separation, emigration. Some loses." ,
"King of Cups":   "A man skilled in law or trade and interested in science, art, religion or philosophy. A good friend, liberal, idealistic and creative. Kind and willing to take some responsibility." , "rdesc" : "A superficial man, easily enthusiastic, but with little depth of character. Untruthful, ruthless and vicious." ,
"Queen of Cups":  "Dreamy, calm, poetic, imaginative, kind yet not willing to take much trouble for another." , "rdesc" : "Dishonest and vicious woman, not to be trusted." ,
"Knight of Cups": "A young man may be an artist, who is graceful and poetic. He is an indolent dreamer of sensual pleasures. Can mean a messenger, a proposition or an invitation." , "rdesc" : "Lazy and deceitful. A dissolute and merciless person." ,
"Page of Cups":  "Quiet and studious youth, but also sweet and dreamy. News or proposition." , "rdesc" : "A sensual libertine, not harmful but neither helpful. Unpleasant news. Flatterer, selfish." ,
"Ace of Cups":  "Harmony, fertility, happiness, beginning of great love." , "rdesc" : "Discord, false love, instability." ,
"Two of Cups":  "Love. Harmony, warm friendship. Close relation with a kindred soul. Good for business and love." , "rdesc" : "Opposition. False love. Folly, misunderstanding." ,
"Three of Cups":  "Abundance. Pleasure, hospitality, success. The good things of life." , "rdesc" : "Sensuality or food and drink intemperance." ,
"Four of Cups":  "Luxury. Abandonment to desire. New ambition." , "rdesc" : "Luxury that does not provide happiness. Dissatisfaction with material success. Turning point in life." ,
"Five of Cups": "Disappointment. Unexpected misfortune. Partial loss. Friendship or love gone. Inheritance." , "rdesc" : "New happiness. Return of an old friend or love. Alliance." ,
"Six of Cups":  "Pleasure. Happiness coming from the past. Nostalgia. Success." , "rdesc" : "Uncertainty. Living too much in the past. Worthless associates. Inheritance." ,
"Seven of Cups":  "Debauch. Foolish expectations. Illusory dreams, deceit. Intoxication. Drug addiction." , "rdesc" : "New will. Intelligent decision. Short travels." ,
"Eight of Cups":  "Indolence. Instability. Material success abandoned, may be for something higher. Decline in interest. Wandering." , "rdesc" : "Joy, happiness. A new love or interest in material things.." ,
"Nine of Cups":   "Happiness. Complete material success and well-being. You will get what you wish." , "rdesc" : "Imperfection, deceit. Intemperance. You will not get what you wish." ,
"Ten of Cups":   "Satiety. Perfect love and lasting contentment. Peace, friendship." , "rdesc" : "Dissipation, loss of friendship. Betrayal. Waste." ,
"King of Swords":   "This man may be a very good ally or counselor. He is clever and self-controlled and has some authority. Also is modern, analytical and very strong. The card may also mean a lawsuit." , "rdesc" : "Deceitful and malicious man. He may be a dangerous enemy, violent and powerful." ,
"Queen of Swords":   "A graceful but stern woman. She has keen insight and good judgment. May be a dancer, a widow or a childless woman. This card also means privation and mourning." , "rdesc" : "Playfully mischievous. Dangerous enemy. Jealous and narrow-minded woman." ,
"Knight of Swords":   "Audacious, clever and gallant; spirited young man. He may be domineering and unstable but he has the better intentions." , "rdesc" : "Harsh, fanatic, extravagant. Tyranic and aggressive. Dangerous enemy." ,
"Page of Swords":  "Logic and penetrating young man or woman. Mentally and physically dexterous. Spying. Messages." , "rdesc" : "Frivolous, revengeful and cunning. Indiscretion. Impotence. Unforeseen perturbation." ,
"Ace of Swords":  "Conquest. Triumph through trouble. Intense activity. Gestation or parturition." , "rdesc" : "Disaster or conquest followed by disaster. Great loss. Violent death. Infertility." ,
"Two of Swords":  "Peace. Balanced forces. Indecision. Strength. Friendship." , "rdesc" : "Disloyalty. Change, sometimes in the wrong direction. Quarrel" ,
"Three of Swords":  "Sorrow. Separation, quarrel, tears. Delay. Absence." , "rdesc" : "Confusion, loss, error." ,
"Four of Swords":  "Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat." , "rdesc" : "Renewed activity. Surprise. Prudence and economy are advised." ,
"Five of Swords":  "Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death." , "rdesc" : "Risk of loss or defeat. Funeral. Weakness." ,
"Six of Swords":  "Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety." , "rdesc" : "Stagnation. Unfavorable result. Intellectual pride." ,
"Seven of Swords": "Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land." , "rdesc" : "Quarrels. Slanders. Disenchantment in family or friendship." ,
"Eight of Swords":  "Interference. Restriction. Temporal sickness or captivity. Indecision." , "rdesc" : "New beginnings. Freedom from the past bondages." ,
"Nine of Swords":  "Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one." , "rdesc" : "Patience, faithfulness, unselfishness." ,
"Ten of Swords":  "Ruin. Total defeat. Death. The end of an illusion." , "rdesc" : "Transitory success. Improvement." ,
"King of Pentacles":  "A married man, wealthy and clever in money matters. Patient and laborious, he is an experimented chief and a reliable ally." , "rdesc" : "Vicious and greedy man. Beware or gamblers or speculators. Easy to bribe, he may be a dangerous man." ,
"Queen of Pentacles":  "Charming and generous woman. Pragmatic and quiet, but ambitious. Opulence, security." , "rdesc" : "Foolish and temperamental. Prone to suspicion ad fearful of failure. Negligent." ,
"Knight of Pentacles":  "Mature and responsible, a trustworthy and laborious man. A capable manager. An important matter concerning money." , "rdesc" : "Dull, lazy or clumsy man. Careless. Stagnation." ,
"Page of Pentacles":  "A learned young person, careful and reflective. Good management, kind and benevolent. The bearer of good news and messages." , "rdesc" : "Wasteful, illogical, rebellious youth. Bad news or lost of money." ,
"Ace of Pentacles":   "The beginning of prosperity and wealth. Pleasure and beauty." , "rdesc" : "Success is delayed or it does not give happiness. Greed." ,
"Two of Pentacles":   "Change. Alternation of gain and loss. Equilibrium in the midst of change. Ability to adapt to new circumstances. Some complications. Unstable mood." , "rdesc" : "Uncertainty. Difficulty adapting to new circumstances." ,
"Three of Pentacles":  "Works. Task well done. Commercial transactions. Professional growth. Dignity. A male child." , "rdesc" : "Unsufficient skill or knowledge to achieve the goal. Fruitless work. Lack of seriousness." ,
"Four of Pentacles":   "Power. Purely material gain and security. A gift or an inheritance. A female child. Greed." , "rdesc" : "Prejudice. Limitation. Sudden check in progress or loss. Reckeless spending of money." ,
"Five of Pentacles":   "Worry. Loss of money or employment. Poverty. Defeat. Lovers. Sympathy found in the midst of trouble." , "rdesc" : "New employment or opportunity. Productive work. Misfortune in love." ,
"Six of Pentacles": "Success. Material gain and power. Sharing with others the wealth." , "rdesc" : "Transitory gains. Prodigality. Bribery. Purse proud." ,
"Seven of Pentacles":  "Failure. Defeat. Loss of money. Hard work but little gain. Greedy." , "rdesc" : "Delayed success after hard work. Work done for the love of work without expecting retribution." ,
"Eight of Pentacles":   "Prudence. The first steps of a profitable profession. Learning a business or profession. Ability in material affairs. A brunette." , "rdesc" : "Greedy. Selfish in a petty way. Vanity." ,
"Nine of Pentacles":   "Gain. Practical wisdom limited to everyday affairs and the home. Stability. Solitude. Inheritance." , "rdesc" : "Loss of friendship or a material thing. Cancelled project. Beware of knavery." ,
"Ten of Pentacles":   "Wealth. Fulfillment of material fortune. Family matters. Inheritance. House." , "rdesc" : "Family misfortune. Loss of inheritance. Beware of risky projects." }




@client.command(description='syntax: x or y', aliases = ['cotd','cunt'])
async def cardundernontsterritory(ctx):
    global listeeee
    global tarotdeck


    dated = datetime.date.today()
    nseed = str(ctx.message.author.id) + "visanu" + str(dated)
    fuck.seed(nseed)
    beyond = str(fuck.choice(listeeee))
    reversed = fuck.randint(0,1)


    if reversed == 0:
        await ctx.send(f'Your card of the day is **{beyond}**\n{tarotdeck[beyond]}')
    else:
        await ctx.send(f'Your card of the day is **{beyond}** reversed')


@client.command()
async def fortune(ctx):
    dated = datetime.date.today()
    nseed = str(ctx.message.author.id) + "Zeus" + str(dated)
    fuck.seed(nseed)
    global bullshit
    resultant = str(fuck.choice(bullshit))
    await ctx.send(resultant)



@client.command()
async def draw(ctx,* ,amount):
    global listeeee
    global tarotdeck
    fuck.seed()
    amount = int(amount)
    drawn = fuck.choices(listeeee,k=amount)
    voi = ""
    c = len(drawn)
    c -= 1

    if amount == 0:
        await ctx.send("What are you trying to acomplish")
    if amount == 1:
        await ctx.send(f"**{drawn[0]}** has been drawn")
    else:
        for temporal in drawn:
            if temporal == drawn[c]:
                check = fuck.randint(0,1)
                if  check == 0:
                    check = "(Reversed)"
                else:
                    check = ""
                voi += f"and {temporal}{check}."
                break
            else:
                check = fuck.randint(0,1)
                if  check == 0:
                    check = "(Reversed)"
                else:
                    check = ""

                voi += temporal
                voi += check
                voi += " ,  "

        await ctx.send(f"I have drawn:    **{voi}**")





@client.command()
async def shame(ctx, member : discord.Member):
    print(ctx.message.mentions[0].id)
    print(discord.Member)
    if str(ctx.message.mentions[0].id) == "307448724089733120":
        await ctx.send(f"I will never insult a Monika's follower or my creator.")

    elif str(ctx.message.mentions[0].id) == "286771477401960450":
        await ctx.send(f"I will never insult a Monika's follower or my creator.")
    else:
        fuck.seed()
        shames = ['You are a... piece of shit!',
        'you..... are... a... bad... person...?',
        'burn in hell you godless barbarian',
        'you should see a neurologist because I think your brain stopped working',
        "Are you there? Sorry I don't see a subhuman like you",
        'You xeno scum',
        'Trash is better than you',
        'A toilet paper will not dissolve as easily as you will',
        'You are good.... for nothing']
        await ctx.send(f"<@{ctx.message.mentions[0].id}>,  {fuck.choice(shames)}")


@client.command()
async def proud(ctx):
    proud = ['I am so proud of you',
    'Nicely done~']
    fuck.seed()
    ctx.send(f'{fuck.choice(proud)}')


@client.command()
async def libra(ctx, member : discord.Member):

    if str(ctx.message.mentions[0].id) == "307448724089733120":

        num1 = "Undefined"
        num2 = "Inconceivable"
        num3 = "Unclear"
        num4 = "Incomprehensible"
        num5 = "Indecipherable"


    else:

        seedd = str(ctx.message.mentions[0].id)+"Holyshit"
        fuck.seed(seedd)
        num1 = fuck.randint(-100, 100)
        num2 = fuck.randint(-100, 100)
        num3 = fuck.randint(-100, 100)
        num4 = fuck.randint(-100, 100)
        num5 = fuck.randint(-200, 100)


    await ctx.send(f'Analysing <@{ctx.message.mentions[0].id}>')
    await ctx.send(f'Intelligence: {num1}')
    await ctx.send(f'Looks: {num2}')
    await ctx.send(f'Friendliness: {num3}')
    await ctx.send(f'Trustworthiness: {num4}')
    await ctx.send(f'Luck: {num5}')

    if (num1+num2+num3+num4+num5) <= -100:
        await ctx.send("My deepest apologies...")

    if (num1+num2+num3+num4+num5) <= 20:
        await ctx.send("I would recommend you to change your identity by consulting your nearest tarot reader person named Nont")

    if num1 == "Undefined":
        await ctx.send("Praise be to my creator!")


@client.command()
async def now(ctx):

    await ctx.send(f"According to the host it's {datetime.datetime.now()}")


@client.command()
async def load(ctx, extension):
    if extension == "DNOP":
        client.load_extension(f'data.{extension}')
        await ctx.send(f'{extension} online, Are you seriously doing this?')
    else:
        client.load_extension(f'data.{extension}')
        await ctx.send(f'{extension} materialized.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'data.{extension}')
    await ctx.send(f'{extension} dematerialized.')



@client.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def r_pung(ctx, member : discord.Member):
    if discord.Member.id == "307448724089733120":
        await ctx.send("What exactly are you trying to do?")

    else:


        await ctx.send(f"Hello motherfucker <@{ctx.message.mentions[0].id}>")
        for x in range (0,5):
            await ctx.send(f"PANG <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PING <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PENG <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PONG <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"Bye bitch <@{ctx.message.mentions[0].id}>")
    #await client.leave_server(message.server)


@client.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def pung(ctx, member : discord.Member):

    if discord.Member.id == "307448724089733120":
        await ctx.send("What exactly are you trying to do?")

    else:
        for x in range (0,4):
            await ctx.send(f"PANG <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PING <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PENG <@{ctx.message.mentions[0].id}>")
            await ctx.send(f"PONG <@{ctx.message.mentions[0].id}>")







@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        fuck.seed()
        ans = ['Failed to complie:\nError event: Lack of additional argument.\nPlease refrain from being brain dead and fill in all the requirements.','Failed to complie:\nError event: Lack of additional argument.']
        ans = fuck.choice(ans)
        await ctx.send(ans)


async def status_change():
    await client.wait_until_ready()
    global stat

    fuck.seed()
    rand = fuck.choice(stat)
    await client.change_presence(status=discord.Status.idle,activity = discord.Game(rand))



@tasks.loop(seconds=10)
async def define():
    global stat

    await client.wait_until_ready()

    fuck.seed()
    rand = fuck.choice(stat)
    await client.change_presence(status=discord.Status.idle,activity = discord.Game(rand))


#jump

@tasks.loop(seconds=1)
async def manual():

    inp = input("ID please: ")
    inp = int(inp)
    channel = client.get_channel(inp)
    await channel.send("Manual override detected. Ceasing fuctions.")
    while True:
        try:
            nepu = input("")
            if nepu == "q":
                manual.stop()
                await channel.send("Resuming auto mode.")
                break
            await channel.send(nepu)
        except:
            print("Exception occured.")

    await client.wait_until_ready()
#nepu = input("")
#await channel.send(nepu)
    #ser= client.get_user(307448724089733120)        #307448724089733120
    #print(f"Sending to {user}")
    #await user.send("Test.")



stored = "これが"

@client.event
async def on_message(message: discord.Message):
    global stored

    if message.content.startswith("st!echo"):
        await message.delete()

    if message.content.startswith("st!true_echo"):
        await message.delete()

    try:
        id = message.guild.id    #exception raiser
        a = (f"{message.author}: '{message.content}' was sent in {message.guild}")
        print(a)

        stored = 1
    except:
        a = (f"{message.author} directed '{message.content}'")
        stored = 1
        print(a)

    #await channel.send(a)
    await client.process_commands(message)


client.run('NzE5MTgyMTYwNjQ4NjAxNjgx.XxfgNg.T2eM0-EpBnfgwAvApIFsrO_rhcQ')
