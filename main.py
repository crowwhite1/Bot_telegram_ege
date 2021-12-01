import logging
import sqlite3
import pathlib
from pathlib import Path
import random
from random import random, randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
API_TOKEN = '2078762775:AAHa_FHvRBUzdJGtTLGqKucBioxdv5NTikM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = sqlite3.connect('polz.db')
cursor = db.cursor()

tabl = sqlite3.connect("predmet/ans.db")
pot = tabl.cursor()




cursor.execute("""CREATE TABLE IF NOT EXISTS users(
id PRIMARY key,
pred TEXT,
sost INT,
verno INT,
vsego INT )""")
db.commit()


import knopki as kb



# @dp.callback_query_handler(lambda c: c.data)
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
#     code = callback_query.data[-1]
#     tg_id = int(callback_query.from_user.id)
#     if code == 'рус':
#         await bot.answer_callback_query(callback_query.id, text='Вы выбрали Русский язык')
#         cursor.execute(f'INSERT INTO users(id,pred) VALUES ({tg_id},"Русский язык")')
#         db.commit()







@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    q = int(message.from_user.id)
    cursor.execute(f"SELECT id FROM users WHERE id == {q}")
    data = cursor.fetchone()
    if data is not None:
        await message.reply('Вы уже зарегистрированы :)')
    else:
        await message.reply("Привет, выбери предметы, которые тебя интересуют?"+"\n"+'Для смены предмета напиши "/change"', reply_markup=kb.keyboard)
        tg_id = int(message.from_user.id)
        try:
            cursor.execute(f'INSERT INTO users(id,pred) VALUES ({tg_id},"0")')
            cursor.execute(f'INSERT INTO stat(id) VALUES ({tg_id})')
        except:
            pass
        cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
        db.commit()
        cursor.execute (f'UPDATE users SET sost = 1 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last1 = 0 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last2 = 0 WHERE id == {tg_id} ')
        db.commit()

@dp.message_handler(commands=['change'])
async def send_change(message: types.Message):
    await message.reply("Выбери предмет, на который желаешь поменять свой выбор", reply_markup=kb.keyboard)
    tg_id = int(message.from_user.id)
    cursor.execute (f'UPDATE users SET sost = 1 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(commands=['statistic'])
async def statist(message: types.Message):



    await message.reply()




@dp.message_handler(Text(equals="Русский язык"))
async def rus(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_rus)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 1 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Математика профиль"))
async def matp(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_matp)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 2 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Математика база"))
async def matb(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_matb)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 3 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Английский язык"))
async def eng(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_eng)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 4 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Немецкий язык"))
async def nem(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_nem)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 5 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Французский язык"))
async def fr(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_fr)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 6 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Испанский язык"))
async def isp(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_isp)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 7 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Физика"))
async def fiz(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_fiz)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 8 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Химия"))
async def him(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_him)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 9 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Биология"))
async def bio(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_bio)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 10 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="География"))
async def geo(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_geo)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 11 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Обществознание"))
async def obsh(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_obsh)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 12 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Литература"))
async def lit(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_lit)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 13 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="История"))
async def ist(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_ist)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 14 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()

@dp.message_handler(Text(equals="Информатика"))
async def inf(message: types.Message):
    await message.reply('Спасибо, за выбор предмета'+'\n'+'Выберите номер задания', reply_markup=kb.nomera_inf)
    tg_id = int(message.from_user.id)
    cursor.execute(f'UPDATE users SET pred = 15 WHERE id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()
@dp.message_handler()
async def zadania(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT pred FROM users WHERE id=={tg_id}')
    pred = cursor.fetchone()
    pred = int(pred[0])
    q = str(randint(1,5))
    cursor.execute(f'SELECT sost FROM users WHERE id=={tg_id}')
    sost = cursor.fetchone()
    sost = int(sost[0])
    if sost==2:
        nomer = str(message.text)
        await  message.reply('Вот ваше задание:')
        await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/zad/"+nomer+"/"+q+".png", 'rb'))
        cursor.execute(f'UPDATE users SET sost = 3 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last1 = {nomer} WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last2 = {q} WHERE id == {tg_id} ')
        db.commit()
    elif sost==3:
        cursor.execute(f'SELECT last1 FROM users WHERE id=={tg_id}')
        last1 = cursor.fetchone()
        last1 = str(last1[0])

        cursor.execute(f'SELECT last2 FROM users WHERE id=={tg_id}')
        last2 = cursor.fetchone()
        last2 = int(last2[0])
        pot.execute(f'SELECT ans FROM ans WHERE (nomer=={int(last1)}) and (zad=={int(last2)}) and (predmet=={int(pred)})')

        p = pot.fetchone()
        ans = str(p[0]).split('/')
        if (pred==1):#русский язык
            if (last2<27):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                #тут нужно вставить отправку критериев!!!!!!!
                await message.reply('Выберите сколько у вас баллов',reply_markup=kb.ball0_25)#
        elif (pred==2):#профиль
            if (last2<12):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                #тут нужно вставить отправку критериев!!!!!!!
                if (last2==12) or (last2==14) or (last2==15):
                    await message.reply('Выберите сколько у вас баллов',reply_markup=kb.ball02)
                elif (last2==13) or (last2==16):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2==17) or (last2==18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
        elif (pred==3):#база
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
        elif (pred==4):#англ
            if (last2<39):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 39):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 40):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball14)
                elif (last2 == 41):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 == 42):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 == 43):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2 == 44):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball10)
        elif (pred==5):#nemeckii
            if (last2<39):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                #тут нужно вставить отправку критериев!!!!!!!
                if (last2==39):
                    await message.reply('Выберите сколько у вас баллов',reply_markup=kb.ball6)
                elif (last2==40):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball14)
                elif (last2==41):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2==42):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2==43):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2==44):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball10)
        elif (pred==6):#franc
            if (last2<39):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 39):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 40):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball14)
                elif (last2 == 41):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 == 42):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2 == 43):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball7)
                elif (last2 == 44):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball7)
        elif (pred==7):#spain
            if (last2<39):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 39):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 40):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball14)
                elif (last2 == 41):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 == 42):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2 == 43):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball7)
                elif (last2 == 44):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball7)
        elif (pred==8):#fizika
            if (last2<24):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
        elif (pred==9):#himia
            if (last2<29):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 31):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 ==32):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2 ==33):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 ==34):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
        elif (pred==10):#biologia
            if (last2<22):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 23):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
        elif (pred==11):#geografia
            if (last2<22) or (last2==23):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 ==25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 ==26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==31):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
        elif (pred==12):
            if (last2<17):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 17):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==19):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==20):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==21):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 ==23):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 ==25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
        elif (pred==13):
            if (last2<5) or (last2 ==7)or (last2 ==8)or (last2 ==9):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 5):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 6):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball8)
                elif (last2 ==10):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 ==11):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball8)
                elif (last2 ==12):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball20)
        elif (pred==14):
            if (last2<12):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                # тут нужно вставить отправку критериев!!!!!!!
                if (last2 == 12):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 13):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==14):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==15):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==16):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==17):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 ==18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 ==19):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
        elif (pred==15):
            if (last2<28):
                if any((message.text)==ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!'+"\n"+"Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open('predmet/'+str(pred)+"/ans/"+last1+"/"+str(last2)+".png", 'rb'))
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()























































































































if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)