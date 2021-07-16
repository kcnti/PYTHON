import discord
import os
from discord.ext import commands
import mysql.connector
import asyncio
from base64 import b64encode
import subprocess
from google_speech import Speech
import requests
from bs4 import BeautifulSoup
import random
import datetime

############### DON'T TOUCH ######################
with open('allowedID.txt') as f:
        allowed_id = [x.rstrip('\n') for x in f]
bot = commands.Bot(command_prefix = ';')
cnt = mysql.connector.connect(user='kanti', password='Kikuanone1234!', host='localhost', database='PSM')
dis = mysql.connector.connect(user='kanti', password='Kikuanone1234!', host='localhost', database='Discord')

############### DON'T TOUCH ######################
_cursor = dis.cursor(buffered=True)
query = "ALTER TABLE account AUTO_INCREMENT = 1"
_cursor.execute(query)
############### DON'T TOUCH ######################

@bot.command()
async def check(ctx):
    print(allowed_id)

def perms(ctx):
    return ctx.author.id == 279970880610893833 or ctx.author.id == 286771477401960450

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    state = "ให้เกียรติพี่หน่อยไอ้น้อง"
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(state))
###################################

#--------------------- SMS

@bot.command()
@commands.has_role('spam permission')
async def abuse(ctx,number,counts):
    phone = number
    count = counts
    await ctx.send(f"Start sending SMS to {phone} with {count} times")
    os.system(f"timeout 10s js Abuse.js {phone} {count}")

#########################################

#---------------------- Accountant
############# DO NOT FORGET TO COMMIT IF YOU WANT TO CHANGE ANYTHING IN MYSQL
lst_commands = {';daily':'daily reward random 0-10 kanCoins per day', ';balance':'check your balance',
        ';commands':'list commands', ';gstinfo':'get student info', ';kspeak':'bot speaker'}


@bot.command()
async def register(ctx):
    # try:
    #   # await ctx.send(ctx.message.author)
    _cursor = dis.cursor(buffered=True)
    count = 0
    date = datetime.datetime.now()
    date = int(date.strftime("%d")) - 1
    query = (f"SELECT name FROM account WHERE name='{ctx.author.id}'")
    _cursor.execute(query)
    for i in _cursor:
        print(i)
        count+=1    

    if count == 0:
        query = ("INSERT INTO account (name, balance, time, times) VALUES (%s, %s, %s, %s)")
        data = (f'{ctx.author.id}', 0, f'{date}', 0)
        _cursor.execute(query, data)
        dis.commit()
        await ctx.send("Register Successful")
        user = bot.get_user(ctx.author.id)
        await user.send('############ Commands ##############\n')
        string = str()
        for key in lst_commands:
            string+=str(key)
            string+=' - '
            string+=str(lst_commands[key])
            string+='\n'
        await user.send(string)
        await user.send('##################################')
    else:
        await ctx.send("Already Registered")
    # except:
    #   await ctx.send("Something went wrong!")

@bot.command()
async def commands(ctx):
    string = str()
    for key in lst_commands:
        string+=str(key)
        string+=' - '
        string+=str(lst_commands[key])
        string+='\n'
    await ctx.send(string)

@bot.command()
async def daily(ctx):
    daily = random.randint(0,10)
    date = datetime.datetime.now()
    _date = date.strftime('%d')
    _cursor = dis.cursor(buffered=True)
    query = (f"SELECT time FROM account WHERE name='{ctx.author.id}'")
    _cursor.execute(query)
    for day in _cursor:
        date = abs(int(_date)-int(day[0]))
    print(date)
    if date >= 1:
        query = (f"UPDATE account SET balance=balance + {daily} WHERE name='{ctx.author.id}';")
        _cursor.execute(query)
        query = (f"UPDATE account SET time={_date} WHERE name='{ctx.author.id}'")
        _cursor.execute(query)
        await ctx.send(f"<@{ctx.author.id}> just got {daily} kanCoins")
        dis.commit()
    else:
        await ctx.send("Not today :)")

@bot.command()
async def gstinfo(ctx, student_id):
    cost = 100
    balance = 0
    _cursor = dis.cursor(buffered=True)
    query = (f"SELECT balance FROM account WHERE name='{ctx.author.id}'")
    _cursor.execute(query)
    for bal in _cursor:
        balance = int(bal[0])-cost
    if balance < 0:
        await ctx.send(f"You need more {abs(balance)} kanCoins")
    else:
        if not student_id.startswith('0'):
                    stnumber = '0'+ student_id
        encoded = b64encode(b64encode(b64encode(student_id.encode('utf-8'))))
        encodedstr = str(encoded, "utf-8")
        if student_id == '019428' or student_id == '021561':
            await ctx.send("Nah Nah")
        else:
            cursor1 = cnt.cursor(buffered=True)
            cursor2 = cnt.cursor(buffered=True)
            query = ("SELECT firstName, lastName, first_name_eng, last_name_eng, Class, idGroupMajors, house_number, moo, street, soi,"
                "alley, district, amphur, postcode, age, weight, height, mobile, email,"
                "lineid, name_father, lastname_father, mobile_farther, lineId_farther, email_farther, name_mother, lastname_mother, mobile_mother, lineId_mother, email_mother FROM student_m2_m5_63 WHERE identitySchoolNumber='" + student_id + "'")
            _query = ("SELECT firstName, lastName, first_name_eng, last_name_eng, Class, idGroupMajors, house_number, moo, street, soi,"
                "alley, district, amphur, postcode, age, weight, height, mobile, email,"
                "lineid, name_father, lastname_father, mobile_farther, lineId_farther, email_farther, name_mother, lastname_mother, mobile_mother, lineId_mother, email_mother FROM student_m4_63 WHERE identitySchoolNumber='" + student_id + "'")
            cursor1.execute(query)
            cursor2.execute(_query)
#           await ctx.send("Fetching from database...")
#           await asyncio.sleep(1)
            for _fname, _lname, _fnameng, _lnameng, _class, idmajor, house_number, moo, street, soi, alley, district, amphur, postcode, age, weight, height, mobile, email, lineid, ffather, lfather, mobile_father, linefather, efather, fmother, lmother, mobile_mother, linemother, emother in cursor2:
                queryAmphur = ("SELECT AMPHUR_ID, AMPHUR_NAME FROM amphur WHERE AMPHUR_ID='"+ amphur +"'")
                queryDistrict = ("SELECT DISTRICT_CODE, DISTRICT_NAME FROM district WHERE DISTRICT_CODE='"+ district +"'")
                queryMajor = ("SELECT id, fullNameGroupMajors from student_major WHERE id='"+ str(idmajor) +"'")
                cursor2.execute(queryMajor)
                for _, __ in cursor2:
                    major = __
                cursor2.execute(queryDistrict)
                for _, _i in cursor2:
                    district = _i
                cursor2.execute(queryAmphur)
                for _, i in cursor2:
                    amphur = i
                await ctx.send(f"> fnameTH: {_fname} {_lname}\n> fnameEN: {_fnameng} {_lnameng}\n> class: ม.{(_class)} {major}\n> house number: {house_number}\n> moo: {moo}\n> street: {street}\n> soi: {soi}\n> alley: {alley}\n> district: {district}\n> amphur: {amphur}\n> postcode: {postcode}\n> age: {age}\n> weight: {weight}\n> height: {height}\n> mobile: {mobile}\n> email: {email}\n> lineid: {lineid}\n> father: {ffather} {lfather}\n> mobile_father: {mobile_father}\n> lineid_father: {linefather}\n> email_father: {efather}\n> mother: {fmother} {lmother}\n> mobile_mother: {mobile_mother}\n> lineid_mother: {linemother}\n> email_mother: {emother}\n> pictures: http://e-psm.net:8091/report/route.php?idcard={encodedstr}")
                await ctx.send(file=discord.File(f'./biophoto/{student_id}.jpg'))
            for _fname, _lname, _fnameng, _lnameng, _class, idmajor, house_number, moo, street, soi, alley, district, amphur, postcode, age, weight, height, mobile, email, lineid, ffather, lfather, mobile_father, linefather, efather, fmother, lmother, mobile_mother, linemother, emother in cursor1:
                queryAmphur = ("SELECT AMPHUR_ID, AMPHUR_NAME FROM amphur WHERE AMPHUR_ID='"+ amphur +"'")
                queryDistrict = ("SELECT DISTRICT_CODE, DISTRICT_NAME FROM district WHERE DISTRICT_CODE='"+ district +"'")
                queryMajor = ("SELECT id, fullNameGroupMajors from student_major WHERE id='"+ str(idmajor) +"'")
                cursor1.execute(queryMajor)
                for _, __ in cursor1:
                    major = __
                cursor1.execute(queryDistrict)
                for _, _i in cursor1:
                    district = _i
                cursor1.execute(queryAmphur)
                for _, i in cursor1:
                    amphur = i
                await ctx.send(f"> fnameTH: {_fname} {_lname}\n> fnameEN: {_fnameng} {_lnameng}\n> class: ม.{int(_class)} {major}\n> house number: {house_number}\n> moo: {moo}\n> street: {street}\n> soi: {soi}\n> alley: {alley}\n> district: {district}\n> amphur: {amphur}\n> postcode: {postcode}\n> age: {age}\n> weight: {weight}\n> height: {height}\n> mobile: {mobile}\n> email: {email}\n> lineid: {lineid}\n> father: {ffather} {lfather}\n> mobile_father: {mobile_father}\n> lineid_father: {linefather}\n> email_father: {efather}\n> mother: {fmother} {lmother}\n> mobile_mother: {mobile_mother}\n> lineid_mother: {linemother}\n> email_mother: {emother}\n> pictures: http://e-psm.net:8091/report/route.php?idcard={encodedstr}")
                await ctx.send(file=discord.File(f'./biophoto/{student_id}.jpg'))
                print(ctx.author, "looking for info of", _fname, _lname)
                query = (f"UPDATE account SET balance=balance-{cost} WHERE name={ctx.author.id}")
                _cursor.execute(query)
                query = (f"UPDATE account SET times=times+1 WHERE name={ctx.author.id}")
                _cursor.execute(query)
                dis.commit()


@bot.command()
async def kspeak(ctx, *, text):
    cost = 1
    _cursor = dis.cursor(buffered=True)
    query = (f"SELECT balance FROM account WHERE name='{ctx.author.id}'")
    _cursor.execute(query)
    for i in _cursor:
        balance = int(i[0]) - cost
    if balance < 0:
        await ctx.send(f"You need more {abs(balance)} kanCoins")
    else: 
        vc = await ctx.author.voice.channel.connect()
        speech = Speech(f"{text}", "th")
        speech.save("output.mp3")
        user = ctx.message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            vc.play(discord.FFmpegPCMAudio(f'./output.mp3'))
            while vc.is_playing():
                await asyncio.sleep(1)
            try:
                await ctx.channel.purge(limit=1)
                await vc.disconnect()
            except:
                await vc.disconnect()
        query = (f"UPDATE account SET balance = balance-{cost} WHERE name='{ctx.author.id}'")
        _cursor.execute(query)
        dis.commit()

@bot.command()
async def balance(ctx):
    _cursor = dis.cursor(buffered=True)
    query = (f"SELECT balance FROM account WHERE name='{ctx.author.id}'")
    _cursor.execute(query)
    for balance in _cursor:
        await ctx.send(f'<@{ctx.author.id}> have {balance[0]} kanCoins')

@bot.command()
async def add_balance(ctx, name, balance):
    name = name[3:-1]
    print(name)
    if ctx.author.id == 279970880610893833:
        _cursor = dis.cursor(buffered=True)
        query = (f"UPDATE account SET balance=balance+{balance} WHERE name='{name}'")
        _cursor.execute(query)
        query = (f"SELECT balance FROM account WHERE name='{name}'")
        _cursor.execute(query)
        for i in _cursor:
            await ctx.send(f"Added balance. Now <@{name}> has {i[0]} kanCoins")
            dis.commit()
    else:
        await ctx.send("จะทำไรหรอ")

# @bot.command()
# async def update_command(ctx):
#   if ctx.author.id == 279970880610893833:
#       _cursor = dis.cursor(buffered=True)
#       query = "SELECT name FROM account"
#       _cursor.execute(query)
#       lst = []
#       for i in _cursor:
#           lst+=(i[0].split())
#       # print(lst)
#       for i in lst:
#           user = bot.get_user(int(i))
#           print(user)
#           await user.send('# Commands\n')
#           await user.send(';daily - daily reward random 0-10 kanCoins per day\n'
#                           ';balance - check your balance\n'
#                           ';gstinfo {student id} - get student info - 100 kanCoins')
#           await user.send('#')

########################################

#---------------------- School things

@bot.command()
async def name(ctx, _class, major):
    try:
        await ctx.send(file=discord.File(f'./name/{_class}-{major}.png'))
        await ctx.send(file=discord.File(f'./name/{_class}-{major}2.png'))
        await ctx.send(file=discord.File(f'./name/{_class}-{major}.jpg'))
        await ctx.send(file=discord.File(f'./name/{_class}-{major}2.jpg'))
    except:
        print("just stupid err")
        raise

@bot.command()
async def list_major(ctx):
    lst = "act animation asian china design eai eng food france iem japan math me mtit music pe rlt sci sci2 sgs".split()
    await ctx.send('\n'.join(lst))

@bot.command()
#@commands.is_owner()
#@commands.has_role('StData')
#@commands.check(perms)
async def stinfo(ctx, stnumber):
    if ctx.author.id in map(int, allowed_id):
        try:
        #   if not commands.checks.has_permissions('StData'):
        #       print("No perms, sry")
            if not stnumber.startswith('0'):
                    stnumber = '0'+ stnumber
            encoded = b64encode(b64encode(b64encode(stnumber.encode('utf-8'))))
            encodedstr = str(encoded, "utf-8")
            if stnumber == '019428' or stnumber == '021561':
                await ctx.send("อะไรวะ")
            else:
                cursor1 = cnt.cursor(buffered=True)
                cursor2 = cnt.cursor(buffered=True)
                query = ("SELECT firstName, lastName, first_name_eng, last_name_eng, Class, idGroupMajors, house_number, moo, street, soi,"
                    "alley, district, amphur, postcode, age, weight, height, mobile, email,"
                    "lineid, name_father, lastname_father, mobile_farther, lineId_farther, email_farther, name_mother, lastname_mother, mobile_mother, lineId_mother, email_mother FROM student_m2_m5_63 WHERE identitySchoolNumber='" + stnumber + "'")
                _query = ("SELECT firstName, lastName, first_name_eng, last_name_eng, Class, idGroupMajors, house_number, moo, street, soi,"
                    "alley, district, amphur, postcode, age, weight, height, mobile, email,"
                    "lineid, name_father, lastname_father, mobile_farther, lineId_farther, email_farther, name_mother, lastname_mother, mobile_mother, lineId_mother, email_mother FROM student_m4_63 WHERE identitySchoolNumber='" + stnumber + "'")
                cursor1.execute(query)
                cursor2.execute(_query)
#               await ctx.send("Fetching from database...")
#               await asyncio.sleep(1)
                for _fname, _lname, _fnameng, _lnameng, _class, idmajor, house_number, moo, street, soi, alley, district, amphur, postcode, age, weight, height, mobile, email, lineid, ffather, lfather, mobile_father, linefather, efather, fmother, lmother, mobile_mother, linemother, emother in cursor2:
                    queryAmphur = ("SELECT AMPHUR_ID, AMPHUR_NAME FROM amphur WHERE AMPHUR_ID='"+ amphur +"'")
                    queryDistrict = ("SELECT DISTRICT_CODE, DISTRICT_NAME FROM district WHERE DISTRICT_CODE='"+ district +"'")
                    queryMajor = ("SELECT id, fullNameGroupMajors from student_major WHERE id='"+ str(idmajor) +"'")
                    cursor2.execute(queryMajor)
                    for _, __ in cursor2:
                        major = __
                    cursor2.execute(queryDistrict)
                    for _, _i in cursor2:
                        district = _i
                    cursor2.execute(queryAmphur)
                    for _, i in cursor2:
                        amphur = i
                    await ctx.send(f"> fnameTH: {_fname} {_lname}\n> fnameEN: {_fnameng} {_lnameng}\n> class: ม.{(_class)} {major}\n> house number: {house_number}\n> moo: {moo}\n> street: {street}\n> soi: {soi}\n> alley: {alley}\n> district: {district}\n> amphur: {amphur}\n> postcode: {postcode}\n> age: {age}\n> weight: {weight}\n> height: {height}\n> mobile: {mobile}\n> email: {email}\n> lineid: {lineid}\n> father: {ffather} {lfather}\n> mobile_father: {mobile_father}\n> lineid_father: {linefather}\n> email_father: {efather}\n> mother: {fmother} {lmother}\n> mobile_mother: {mobile_mother}\n> lineid_mother: {linemother}\n> email_mother: {emother}\n> pictures: http://e-psm.net:8091/report/route.php?idcard={encodedstr}")
                    await ctx.send(file=discord.File(f'./biophoto/{stnumber}.jpg'))
                for _fname, _lname, _fnameng, _lnameng, _class, idmajor, house_number, moo, street, soi, alley, district, amphur, postcode, age, weight, height, mobile, email, lineid, ffather, lfather, mobile_father, linefather, efather, fmother, lmother, mobile_mother, linemother, emother in cursor1:
                    queryAmphur = ("SELECT AMPHUR_ID, AMPHUR_NAME FROM amphur WHERE AMPHUR_ID='"+ amphur +"'")
                    queryDistrict = ("SELECT DISTRICT_CODE, DISTRICT_NAME FROM district WHERE DISTRICT_CODE='"+ district +"'")
                    queryMajor = ("SELECT id, fullNameGroupMajors from student_major WHERE id='"+ str(idmajor) +"'")
                    cursor1.execute(queryMajor)
                    for _, __ in cursor1:
                        major = __
                    cursor1.execute(queryDistrict)
                    for _, _i in cursor1:
                        district = _i
                    cursor1.execute(queryAmphur)
                    for _, i in cursor1:
                        amphur = i
                    await ctx.send(f"> fnameTH: {_fname} {_lname}\n> fnameEN: {_fnameng} {_lnameng}\n> class: ม.{int(_class)} {major}\n> house number: {house_number}\n> moo: {moo}\n> street: {street}\n> soi: {soi}\n> alley: {alley}\n> district: {district}\n> amphur: {amphur}\n> postcode: {postcode}\n> age: {age}\n> weight: {weight}\n> height: {height}\n> mobile: {mobile}\n> email: {email}\n> lineid: {lineid}\n> father: {ffather} {lfather}\n> mobile_father: {mobile_father}\n> lineid_father: {linefather}\n> email_father: {efather}\n> mother: {fmother} {lmother}\n> mobile_mother: {mobile_mother}\n> lineid_mother: {linemother}\n> email_mother: {emother}\n> pictures: http://e-psm.net:8091/report/route.php?idcard={encodedstr}")
                    await ctx.send(file=discord.File(f'./biophoto/{stnumber}.jpg'))
                    print(ctx.author, "looking for info of", _fname, _lname)
        except (mysql.connector.Error, FileNotFoundError) as err:
            print(err)
            raise
    else:
        await ctx.send("ถามเทพเอิร์ธดูนะว่าให้รึเปล่า อิอิ")

@bot.command()
async def stname(ctx, name):
    try:
        cursor1 = cnt.cursor(buffered=True)
        cursor2 = cnt.cursor(buffered=True)
        query = ("SELECT identitySchoolNumber, firstName, lastName, first_name_eng, last_name_eng, mobile, email, lineId FROM student_m2_m5_63 WHERE firstName='" + name + "'")
        cursor1.execute(query)
        query2 = ("SELECT identitySchoolNumber, firstName, lastName, first_name_eng, last_name_eng, mobile, email, lineId FROM student_m4_63 WHERE firstName='" + name + "'")
        cursor2.execute(query2)
        for idsn, fn, ln, fne, lne, mb, em, line in cursor1:
            await ctx.send(f"> st_id: {idsn}\n> name_th: {fn} {ln}\n> name_en: {fne} {lne}\n> mobile: {mb}\n> email: {em}\n> line: {line}")
            await ctx.send(file=discord.File(f'./biophoto/{idsn}.jpg'))
        for idsn, fn, ln, fne, lne, mb, em, line in cursor2:
            await ctx.send(f"> st_id: {idsn}\n> name_th: {fn} {ln}\n> name_en: {fne} {lne}\n> mobile: {mb}\n> email: {em}\n> line: {line}")
            await ctx.send(file=discord.File(f'./biophoto/{idsn}.jpg'))
    except (mysql.connector.Error, FileNotFoundError) as err:
        print(err)
        raise
############################################

#-------------- Discord connection

@bot.command()
async def connect(ctx):
    await ctx.author.voice.channel.connect()

@bot.command()
async def ps(ctx, song, amount=1):
    if ctx.author.id in map(int, allowed_id):
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(f'./sound/{song}.mp3'))
        await asyncio.sleep(1)
        while vc.is_playing():
            await asyncio.sleep(1)
        try:
                await ctx.channel.purge(limit=1)
                await vc.disconnect()
        except:
                await vc.disconnect()
    else:
        vc = await ctx.author.voice.channel.connect()
        await ctx.channel.purge(limit=1)
        user = ctx.message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            vc.play(discord.FFmpegPCMAudio(f'./lnwearth.mp3'))
            while vc.is_playing():
                await asyncio.sleep(1)
            try:
                await ctx.channel.purge(limit=1)
                await vc.disconnect()
            except:
                await vc.disconnect()

@bot.command()
async def loopconn(ctx, loop):
    _loop = int(loop)
    conn = ctx.author.voice.channel
    for i in range(_loop):
        await conn.connect()
        #asyncio.sleep(0.5)
        await ctx.voice_client.disconnect()

@bot.command()
async def list_sound(ctx):
    lst_sound = []
    for i in os.listdir('./sound'):
        _ = os.path.splitext(i)[0]
        lst_sound.append(_)
    joined = '\n'.join(lst_sound)
    await ctx.send(joined)
@bot.command()
async def dc(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def speaken(ctx, *, text):
    if ctx.author.id in map(int, allowed_id):
        vc = await ctx.author.voice.channel.connect()
        print(ctx.author.nick)
        speech = Speech(f"{text}", "en")
        speech.save("output.mp3")
        user = ctx.message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            vc.play(discord.FFmpegPCMAudio(f'./output.mp3'))
            while vc.is_playing():
                await asyncio.sleep(1)
            try:
                await ctx.channel.purge(limit=1)
                await vc.disconnect()
            except:
                await vc.disconnect()
        else:
            vc = await ctx.author.voice.channel.connect()
            user = ctx.message.author
            voice_channel = user.voice.channel
            channel = None
            if voice_channel != None:
                vc.play(discord.FFmpegPCMAudio(f'./lnwearth.mp3'))
                while vc.is_playing():
                    await asyncio.sleep(1)
                try:
                    await ctx.channel.purge(limit=1)
                    await vc.disconnect()
                except:
                    await vc.disconnect()

@bot.command()
#@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def clear(ctx, amount=1):
    try:
        await ctx.send(f"Removing {amount} messages")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=amount+2)
    except ValueError:
        await ctx.send("No permission!")

@bot.command()
#@commands.has_role('spam permission')
#@commands.has_role('King TEE ติงเปรี๊ยะ')
async def spam(ctx, member : discord.Member, text, rounds):
    if discord.Member.id == "279970880610893833":
        await ctx.send("Sorry this is my own bot :)")
    _round = int(rounds)
    await ctx.send('> `spam with {} loops`'.format(_round))
#    await bot.delete_message(ctx.message)
    for x in range (_round):
        await ctx.send(f"{text} <@{ctx.message.mentions[0].id}>")

@bot.command()
async def dm(ctx, member : discord.Member, message, loop):
    for i in range(int(loop)):
        user = bot.get_user(int(ctx.message.mentions[0].id))
        await user.send(message)
###################################################

#------------------- Perms manager

@bot.command()
async def add_id(ctx, id):
    if ctx.author.id == 279970880610893833:
        with open('allowedID.txt', 'a') as f:
            f.write(f"{id}\n")
        f.close()
        allowed_id.append(id)
        await ctx.send(f"Added id: {id}")
    else:
        await ctx.send("ไปขอร้องอ้อนวอนต่อเทพเอิร์ธนะ")

@bot.command()
async def update_id(ctx):
    global allowed_id
    with open('allowedID.txt') as f:
        allowed_id = [x.rstrip('\n') for x in f]
    output = ', '.join(allowed_id)
    await ctx.send(f'allowed_id:\n{output}')


@bot.command()
async def drop_id(ctx, id):
    if ctx.author.id == 279970880610893833:
        allowed_id.remove(id)
    else:
        await ctx.send("nothing to do")

@bot.command()
async def speak(ctx, *, text):
    if ctx.author.id in 279970880610893833:
        vc = await ctx.author.voice.channel.connect()
        print(ctx.author.nick)
        speech = Speech(f"{text}", "th")
        speech.save("output.mp3")
        user = ctx.message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            vc.play(discord.FFmpegPCMAudio(f'./output.mp3'))
            while vc.is_playing():
                await asyncio.sleep(1)
            try:
                await ctx.channel.purge(limit=1)
                await vc.disconnect()
            except:
                await vc.disconnect()
    else:
        await ctx.send("Please use ;kspeak!")

#       vc = await ctx.author.voice.channel.connect()
#       user = ctx.message.author
#       voice_channel = user.voice.channel
#       channel = None
#       if voice_channel != None:
#           vc.play(discord.FFmpegPCMAudio(f'./lnwearth.mp3'))
#           while vc.is_playing():
#           await asyncio.sleep(1)
#           try:
#               await ctx.channel.purge(limit=1)
#               await vc.disconnect()
#           except:
#               await vc.disconnect()
##############################################

#--------------------- ETC

@bot.command()
async def rkick(ctx, member : discord.Member, *, reason="Cxnt"):
    await member.kick(reason=reason)

@bot.command()
async def bots(ctx):
    await ctx.send(f"Me")

@bot.command()
async def โหน่ง(ctx):
    await ctx.send(f"โหน่ง : สถานะ ตายแล้ว")

@bot.command()
async def tonether(ctx,x,y,z):
    nx = (12/100)*float(x)
    nz = (12/100)*float(z)
    await ctx.send(f'Nether coordinate calc\nx = {nx}\ny = {y}\nz = {nz}')

@bot.command()
async def r6stats(ctx, name):
    url = requests.get(f'https://r6.tracker.network/profile/pc/{name}')
    soup = BeautifulSoup(url.content, 'html.parser')
    stats = soup.find('div', {'class':'trn-scont__content'}).get_text('\n', strip=True)
    await ctx.send(f'{stats}')

bot.run('NzM3NjAyNDY4MzM4NDY2ODE2.Xx_v1A.3PQ_5kbIaOkAGR7BQC4ZM4fWzEk')





#---------------- Trash


#ถามเทพเอิร์ธดูนะว่าให้รึเปล่า
"""@bot.event
async def on_message(message: discord.Message):
    try:
        mes = (f"{message.author}: '{message.content}' was sent in server {message.guild} in channel {message.channel.name}")
        print(mes)
        user = bot.get_user(279970880610893833)
        await user.send(mes)
        #channel = bot.get_channel(769436332468338728)
        #await channel.send(mes)
    except:
        mes = (f"{message.author} directed '{message.content}'")
        print(mes)
        #raise

@commands.Cog.listener()
async def on_message_delete(self, c):
    if(c.guild):
        if c.guild.name == "BotHia":
            channel = bot.get_channel(769436332468338728)
            if c.author.bot == True:
                mes = (f"Bot: {c.author} deleted --- {c.clean_content} --- in #{c.channel.name}")
                await channel.send(mes)
            else:
                mes = (f"User: {c.author} deleted --- {c.clean_content} --- in #{c.channel.name}")
                await channel.send(mes)"""
