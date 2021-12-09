import logging
import sqlite3
import pathlib
from pathlib import Path
import random
from knopki import d
from random import random, randint
from aiogram import Bot, Dispatcher, executor, types
from pyqiwip2p import QiwiP2P
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Text
YTOKEN = '381764678:TEST:31528'
API_TOKEN = '2078762775:AAHa_FHvRBUzdJGtTLGqKucBioxdv5NTikM'
p2p = QiwiP2P(auth_key='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Im9qYmF3bi0wMCIsInVzZXJfaWQiOiI3OTg4NTU1ODU5NiIsInNlY3JldCI6IjgzNmZlNzQ4MDA2ODFkMWIzZmNmNGZjMGUwNDM5NDMxOGFiNzE2Y2JlNTdjODdmNTk1YTY3ZDRkZGNlY2FlZmQifX0=')
#48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPv7hb9epaxFxZiGyJF3dUWoPRZBaGB1Ycf4jUuR65eH1eUAPgSZMcjgNTcRBaY5vUmBbPS58xQRPCWfVPsrqEuN96j444Jamr2i4yC1JeB
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = sqlite3.connect('polz.db')
cursor = db.cursor()

tabl = sqlite3.connect("predmet/ans.db")
pot = tabl.cursor()

reply_rus = KeyboardButton('Русский язык')
reply_matp = KeyboardButton('Математика профиль')
reply_matb = KeyboardButton('Математика база')
reply_en = KeyboardButton('Английский язык')
reply_nem = KeyboardButton('Немецкий язык')
reply_fr = KeyboardButton('Французский язык')
reply_spa = KeyboardButton('Испанский язык')
reply_fiz = KeyboardButton('Физика')
reply_him = KeyboardButton('Химия')
reply_bio = KeyboardButton('Биология')
reply_geo = KeyboardButton('География')
reply_obsh = KeyboardButton('Обществознание')
reply_lit = KeyboardButton('Литература')
reply_ist = KeyboardButton('История')
reply_inf = KeyboardButton('Информатика')
reply_drug = KeyboardButton('Другой предмет')

q = [0, reply_rus, reply_matp, reply_matb, reply_en, reply_nem, reply_fr, reply_spa, reply_fiz, reply_him, reply_bio,
     reply_geo, reply_obsh, reply_lit,
     reply_ist, reply_inf, reply_drug]

import knopki as kb


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
def add_check(user_id, bill_id):
    return cursor.execute(f'INSERT INTO check_bill(id,bill_id) values({user_id}, {bill_id})')
def get_check(bill_id):
    result = cursor.execute(f'select * from check_bill where bill_id=?',(bill_id,)).fetchmany(1)
    if not bool(len(result)):
        return False
    else:
        return int(result[0][0])
def delete_check(bill_id):
    return cursor.execute(f'delete from check_bill where bill_id=?', (bill_id,))




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    q = int(message.from_user.id)
    cursor.execute(f"SELECT id FROM users WHERE id == {q}")
    data = cursor.fetchone()
    if data is not None:
        await message.reply('Вы уже зарегистрированы :)')
    else:
        await message.reply(
            "Привет, выбери предметы, которые тебя интересуют?" + "\n" + 'Для смены предмета напиши "/change"',
            reply_markup=kb.keyboard)
        tg_id = int(message.from_user.id)
        try:
            cursor.execute(f'INSERT INTO users(id,pred) VALUES ({tg_id},"0")')
            cursor.execute(f'INSERT INTO stat(id) VALUES ({tg_id})')
        except:
            pass
        cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
        db.commit()
        cursor.execute(f'UPDATE users SET sost = 1 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last1 = 0 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last2 = 0 WHERE id == {tg_id} ')
        db.commit()


@dp.message_handler(commands=['change'])
async def send_change(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3 FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    # print(a)
    if a[0] == 0:
        if a[1] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]])
        else:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(reply_drug)
    elif a[0] == 1:
        if a[1] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]])
        else:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(reply_drug)
        if a[2] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[2]])
        else:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(reply_drug)
    elif a[0] == 2:
        if a[1] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]])
        else:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(reply_drug)
        if a[2] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(q[a[2]])
        else:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(reply_drug)
        if a[3] != 'None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(q[a[2]]).add(
                q[a[3]])
        elif (a[2]!='None') and (a[3]=='None'):
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(q[a[2]]).add(
                reply_drug)
        elif a[2]=='None':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(q[a[1]]).add(reply_drug).add(
                reply_drug)

    if a[0]!=0:
        await message.reply("Выбери предмет, на который желаешь поменять свой выбор", reply_markup=keyboard)
        cursor.execute(f'UPDATE users SET sost = 5 WHERE id == {tg_id} ')
        db.commit()
    else:
        await message.reply('Вам недоступна смена предмета. Чтобы разблокировать другой предмет напишите "/donat"')
        cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
        db.commit()

@dp.message_handler(commands=['donat'])
async def donat(message: types.Message):
    await message.reply('Возможные варианты доната:'+'\n'+'Произвольная сумма на карту:'+'\n'+'2200 2404 4873 3218'+'\n'+'Купить дополнительные предметы'+'\n'+'Если у вас уже куплено 2 дополнительных предмета, то больше добавить мы, к сожалению не сможем, покупка будет расценена, как пожертвование ', reply_markup=kb.pred1_inline_markup)
@dp.callback_query_handler(text="pred1")
async def pred1(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    #await bot.send_invoice(chat_id=call.from_user.id,title="Покупка дополнительного предмета",description='Доп. предмет',payload='pred',
    #                        provider_token=YTOKEN,currency='RUB',start_parameter='text',prices=[{"label":"Рубли", "amount": 7400}])
    comment = str(call.from_user.id) + '_'+ str(randint(1000,10000))
    bill = p2p.bill(amount=1, lifetime=15,comment=comment)
    s= str(bill.bill_id)
    #print(s)
    cursor.execute(f'INSERT INTO check_bill(id,bill_id) values (?,?)', (call.from_user.id, s,))
    db.commit()
    await bot.send_message(call.from_user.id, "Вам необходимо отправить 30 рублей на наш счёт QIWI"+"\n"+"По ссылке: "+str(bill.pay_url)+"\n"+"Указав в комментарии к оплате: "+str(comment),
                           reply_markup=kb.buy_menu(url=bill.pay_url, bill=bill.bill_id) )

@dp.callback_query_handler(text_contains = "check_")
async def pred2(call: types.CallbackQuery):
    bill = str(call.data).replace('check_','')
    info = get_check(bill)
    cursor.execute(f'SELECT donat from users where id == {call.from_user.id}')
    p = cursor.fetchone()
    p = int(p[-1])
    if info!= False:
        if str(p2p.check(bill_id=bill).status == 'PAID'):
            if p == 0:
                await bot.send_message(call.from_user.id,
                                            'Вы купили дополнительные предметы. Напишите "/change", чтобы добавить их себе')
                cursor.execute(f'UPDATE users SET donat = 2 WHERE id == {call.from_user.id} ')
                delete_check(bill)
                db.commit()
            else:
                await bot.send_message(call.from_user.id,'К сожалению нельзя купить больше 2 дополнительных предметов.')
        else:
            bot.send_message(call.from_user.id,"Вы не оплатили счёт!")
    else:
        await bot.send_message(call.from_user.id, 'Счёт не найден')



@dp.message_handler(commands=['statistic'])
async def statist(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(
        f'SELECT pred1_prav,pred1_vsego,pred2_prav,pred2_vsego,pred3_prav,pred3_vsego FROM stat WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        a[i] = int(a[i])
    cursor.execute(f'SELECT donat from users where id == {tg_id}')
    p = cursor.fetchone()
    p = int(p[-1])
    if p == 0:
        cursor.execute(f'SELECT pred1 from users where id == {tg_id}')
        q = cursor.fetchone()
        q = int(q[-1])
        await message.reply(
            'Вот Ваша статистика по предмету (задания второй части не учитываются)' + '\n' + str(d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%')
    elif p == 1:
        cursor.execute(f'SELECT pred1 from users where id == {tg_id}')
        q = cursor.fetchone()
        q = int(q[-1])
        if q[-1]!=None:
            q = int(q[-1])
        else: q[-1] = 'None'
        cursor.execute(f'SELECT pred2 from users where id == {tg_id}')
        v = cursor.fetchone()
        v[-1] = int(v[-1])
        await message.reply(
            'Вот Ваша статистика по предметам (задания второй части не учитываются)' + '\n' + str(d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%' + '\n' + str(d[v]) + ':' + '\n' + str(
                a[2]) + " из " + str(
                a[3]) + ' или же ' + str(toFixed(a[2] / a[3] * 100, 2)) + '%')
    elif p == 2:
        cursor.execute(f'SELECT pred1 from users where id == {tg_id}')
        q = cursor.fetchone()
        q = int(q[-1])
        cursor.execute(f'SELECT pred2 from users where id == {tg_id}')
        v = list(cursor.fetchone())
        if v[-1]!=None:
            v[-1] = int(v[-1])
        else: v[-1] = 'None'
        cursor.execute(f'SELECT pred3 from users where id == {tg_id}')
        t = list(cursor.fetchone())
        if t[-1]!=None:
            t[-1] = int(t[-1])
        else: t[-1]='None'
        if v[-1]=='None':
            await message.reply(
            'Вот Ваша статистика по предметам (задания второй части не учитываются)' + '\n' + str(d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%')
        elif (v[-1]!='None') and (t[-1]=='None'):
            await message.reply(
                'Вот Ваша статистика по предметам (задания второй части не учитываются)' + '\n' + str(
                    d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                    a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%' + '\n' + str(d[v[-1]]) + ':' + '\n' + str(
                    a[2]) + " из " + str(
                    a[3]) + ' или же ' + str(toFixed(a[2] / a[3] * 100, 2)) + '%')
        elif t[-1]!='None':
            if a[5]==0:
                await message.reply(
            'Вот Ваша статистика по предметам (задания второй части не учитываются)' + '\n' + str(d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%' + '\n' + str(d[v[-1]]) + ':' + '\n' + str(
                a[2]) + " из " + str(
                a[3]) + ' или же ' + str(toFixed(a[2] / a[3] * 100, 2)) + '%' + '\n' + str(d[t[-1]]) + ':' + '\n' + str(
                a[4]) + " из " + str(
                a[5]) + ' или же '+ '0%')
            else:
                await message.reply(
                    'Вот Ваша статистика по предметам (задания второй части не учитываются)' + '\n' + str(
                        d[q]) + ':' + '\n' + str(a[0]) + " из " + str(
                        a[1]) + ' или же ' + str(toFixed(a[0] / a[1] * 100, 2)) + '%' + '\n' + str(
                        d[v[-1]]) + ':' + '\n' + str(
                        a[2]) + " из " + str(
                        a[3]) + ' или же ' + str(toFixed(a[2] / a[3] * 100, 2)) + '%' + '\n' + str(
                        d[t[-1]]) + ':' + '\n' + str(
                        a[4]) + " из " + str(
                        a[5]) + ' или же ' + str(toFixed(a[4] / a[5] * 100, 2)) + '%')


@dp.message_handler(Text(equals="Русский язык"))
async def rus(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(1 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_rus)
            cursor.execute(f'UPDATE users SET pred = 1 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_rus)
        cursor.execute(f'UPDATE users SET pred = 1 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 1 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_rus)
                cursor.execute(f'update users set pred =1 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =1 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_rus)
                cursor.execute(f'update users set pred =1 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =1 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_rus)
                cursor.execute(f'update users set pred =1 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =1 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Математика профиль"))
async def matp(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(2 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_matp)
            cursor.execute(f'UPDATE users SET pred = 2 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_matp)
        cursor.execute(f'UPDATE users SET pred = 2 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 2 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matp)
                cursor.execute(f'update users set pred =2 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =2 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matp)
                cursor.execute(f'update users set pred =2 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =2 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matp)
                cursor.execute(f'update users set pred =2 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =2 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Математика база"))
async def matb(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(3 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_matb)
            cursor.execute(f'UPDATE users SET pred = 3 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_matb)
        cursor.execute(f'UPDATE users SET pred = 3 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 3 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matb)
                cursor.execute(f'update users set pred =3 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =3 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matb)
                cursor.execute(f'update users set pred =3 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =3 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_matb)
                cursor.execute(f'update users set pred =3 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =3 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Английский язык"))
async def eng(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(4 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_eng)
            cursor.execute(f'UPDATE users SET pred = 4 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_eng)
        cursor.execute(f'UPDATE users SET pred = 4 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 4 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_eng)
                cursor.execute(f'update users set pred =4 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =4 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_eng)
                cursor.execute(f'update users set pred =4 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =4 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_eng)
                cursor.execute(f'update users set pred =4 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =4 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Немецкий язык"))
async def nem(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(5 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_nem)
            cursor.execute(f'UPDATE users SET pred = 5 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_nem)
        cursor.execute(f'UPDATE users SET pred = 5 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 5 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_nem)
                cursor.execute(f'update users set pred =5 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =5 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_nem)
                cursor.execute(f'update users set pred =5 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =5 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_nem)
                cursor.execute(f'update users set pred =5 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =5 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Французский язык"))
async def fr(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(6 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_fr)
            cursor.execute(f'UPDATE users SET pred = 6 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_fr)
        cursor.execute(f'UPDATE users SET pred = 6 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 6 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fr)
                cursor.execute(f'update users set pred =6 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =6 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fr)
                cursor.execute(f'update users set pred =6 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =6 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fr)
                cursor.execute(f'update users set pred =6 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =6 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Испанский язык"))
async def isp(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(7 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_isp)
            cursor.execute(f'UPDATE users SET pred = 7 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_isp)
        cursor.execute(f'UPDATE users SET pred = 7 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 7 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_isp)
                cursor.execute(f'update users set pred =7 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =7 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_isp)
                cursor.execute(f'update users set pred =7 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =7 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_isp)
                cursor.execute(f'update users set pred =7 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =7 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Физика"))
async def fiz(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(8 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_fiz)
            cursor.execute(f'UPDATE users SET pred = 8 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_fiz)
        cursor.execute(f'UPDATE users SET pred = 8 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 8 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fiz)
                cursor.execute(f'update users set pred =8 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =8 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fiz)
                cursor.execute(f'update users set pred =8 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =8 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_fiz)
                cursor.execute(f'update users set pred =8 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =8 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Химия"))
async def him(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(9 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_him)
            cursor.execute(f'UPDATE users SET pred = 9 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_him)
        cursor.execute(f'UPDATE users SET pred = 9 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 9 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_him)
                cursor.execute(f'update users set pred =9 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =9 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_him)
                cursor.execute(f'update users set pred =9 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =9 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_him)
                cursor.execute(f'update users set pred =9 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =9 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Биология"))
async def bio(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(10 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_bio)
            cursor.execute(f'UPDATE users SET pred = 1 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_bio)
        cursor.execute(f'UPDATE users SET pred = 10 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 10 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_bio)
                cursor.execute(f'update users set pred =10 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =10 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_bio)
                cursor.execute(f'update users set pred =10 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =10 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_bio)
                cursor.execute(f'update users set pred =1 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =1 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="География"))
async def geo(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(11 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_geo)
            cursor.execute(f'UPDATE users SET pred = 11 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_geo)
        cursor.execute(f'UPDATE users SET pred = 11 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 11 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_geo)
                cursor.execute(f'update users set pred =11 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =11 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_geo)
                cursor.execute(f'update users set pred =11 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =11 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_geo)
                cursor.execute(f'update users set pred =11 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =11 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Обществознание"))
async def obsh(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(12 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_obsh)
            cursor.execute(f'UPDATE users SET pred = 12 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_obsh)
        cursor.execute(f'UPDATE users SET pred = 12 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 12 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_obsh)
                cursor.execute(f'update users set pred =12 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =12 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_obsh)
                cursor.execute(f'update users set pred =12 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =12 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_obsh)
                cursor.execute(f'update users set pred =12 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =12 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Литература"))
async def lit(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(13 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_lit)
            cursor.execute(f'UPDATE users SET pred = 1 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_lit)
        cursor.execute(f'UPDATE users SET pred = 13 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 13 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_lit)
                cursor.execute(f'update users set pred =13 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =13 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_lit)
                cursor.execute(f'update users set pred =13 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =13 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_lit)
                cursor.execute(f'update users set pred =13 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =13 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="История"))
async def ist(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(14 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_ist)
            cursor.execute(f'UPDATE users SET pred = 14 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_ist)
        cursor.execute(f'UPDATE users SET pred = 14 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 14 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_ist)
                cursor.execute(f'update users set pred =14 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =14 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_ist)
                cursor.execute(f'update users set pred =14 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =14 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_ist)
                cursor.execute(f'update users set pred =14 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =14 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Информатика"))
async def inf(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    if a[4] == 5:
        if any(15 == a[i] for i in range(1, 4)):
            await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                reply_markup=kb.nomera_inf)
            cursor.execute(f'UPDATE users SET pred = 15 WHERE id == {tg_id} ')
        else:
            await message.reply('Вы не можете выбрать русский язык')
    if a[4] == 1:
        await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания', reply_markup=kb.nomera_inf)
        cursor.execute(f'UPDATE users SET pred = 15 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET pred1 = 15 WHERE id == {tg_id} ')
    if a[4] == 6:
        if a[0] == 0:
            await message.reply(
                'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
        if a[0] == 1:
            if a[2] != "None":
                await message.reply(
                    'Вы уже не можете бесплатно сменить предмет. Для разблокировки дополнительных предметов воспользуйтесь командой "/donat"')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_inf)
                cursor.execute(f'update users set pred =15 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =15 where id == {tg_id}')
        if a[0] == 2:
            if a[2] == "None":
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_inf)
                cursor.execute(f'update users set pred =15 where id == {tg_id}')
                cursor.execute(f'update users set pred2 =15 where id == {tg_id}')
            elif a[3] != "None":
                await message.reply(
                    'Вы больше не можете добавить предмет. Придётся выбирать из имеющихся')
            else:
                await message.reply('Спасибо, за выбор предмета' + '\n' + 'Выберите номер задания',
                                    reply_markup=kb.nomera_inf)
                cursor.execute(f'update users set pred =15 where id == {tg_id}')
                cursor.execute(f'update users set pred3 =15 where id == {tg_id}')
    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler(Text(equals="Другой предмет"))
async def inf(message: types.Message):
    tg_id = message.from_user.id
    await message.reply(
        "Привет, выбери предметы, которые тебя интересуют?" + "\n" + 'Для смены предмета напиши "/change"',
        reply_markup=kb.keyboard)
    cursor.execute(f'UPDATE users SET sost = 6 WHERE id == {tg_id} ')
    db.commit()


@dp.message_handler()
async def zadania(message: types.Message):
    tg_id = int(message.from_user.id)
    cursor.execute(f'SELECT pred FROM users WHERE id=={tg_id}')
    pred = cursor.fetchone()
    pred = int(pred[0])
    q = str(randint(1, 5))
    cursor.execute(f'SELECT sost FROM users WHERE id=={tg_id}')
    sost = cursor.fetchone()
    sost = int(sost[0])
    cursor.execute(f'SELECT donat,pred1,pred2,pred3,sost FROM users WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    a = p.split(',')
    for i in range(len(a)):
        if a[i] != 'None':
            a[i] = int(a[i])
    cursor.execute(
        f'SELECT pred1_prav,pred1_vsego,pred2_prav,pred2_vsego,pred3_prav,pred3_vsego FROM stat WHERE id == {tg_id}')
    p = str(cursor.fetchone())
    p = p.replace(' ', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    b = p.split(',')
    for i in range(len(b)):
        if b[i] != 'None':
            b[i] = int(b[i])
    if sost == 2:
        nomer = str(message.text)
        await  message.reply('Вот ваше задание:')
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('predmet/' + str(pred) + "/zad/" + nomer + "/" + q + ".png", 'rb'))
        cursor.execute(f'UPDATE users SET sost = 3 WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last1 = {nomer} WHERE id == {tg_id} ')
        cursor.execute(f'UPDATE users SET last2 = {q} WHERE id == {tg_id} ')
        db.commit()
    elif sost == 3:
        cursor.execute(f'SELECT last1 FROM users WHERE id=={tg_id}')
        last1 = cursor.fetchone()
        last1 = str(last1[0])

        cursor.execute(f'SELECT last2 FROM users WHERE id=={tg_id}')
        last2 = cursor.fetchone()
        last2 = int(last2[0])
        pot.execute(
            f'SELECT ans FROM ans WHERE (nomer=={int(last1)}) and (zad=={int(last2)}) and (predmet=={int(pred)})')

        p = pot.fetchone()
        ans = str(p[0]).split('/')
        if (pred == 1):  # русский язык
            if (last2 < 27):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==1:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==1:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==1:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 1:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 1:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 1:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball0_25)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 2):  # профиль
            if (last2 < 12):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==2:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==2:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==2:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 2:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 2:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 2:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 12) or (last2 == 14) or (last2 == 15):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 13) or (last2 == 16):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 17) or (last2 == 18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 3):  # база
            if any((message.text) == ans[i] for i in range(len(ans))):
                await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                await bot.send_photo(chat_id=message.chat.id,
                                     photo=open('predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png",
                                                'rb'))
                if a[1] == 3:
                    b[0] += 1
                    b[1] += 1
                    cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                    cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                    db.commit()
                elif a[2] == 3:
                    b[2] += 1
                    b[3] += 1
                    cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                    cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                    db.commit()
                elif a[3] == 3:
                    b[4] += 1
                    b[5] += 1
                    cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                    cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                    db.commit()
                cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                db.commit()
                cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                db.commit()
            else:
                await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                await bot.send_photo(chat_id=message.chat.id,
                                     photo=open('predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png",
                                                'rb'))
                if a[1] == 3:
                    b[1] += 1
                    cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                    db.commit()
                elif a[2] == 3:
                    b[3] += 1
                    cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                    db.commit()
                elif a[3] == 3:
                    b[5] += 1
                    cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                    db.commit()
                cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 4):  # англ
            if (last2 < 39):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==4:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==4:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==4:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 4:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 4:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 4:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
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
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 5):  # nemeckii
            if (last2 < 39):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==5:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==5:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==5:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 5:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 5:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 5:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
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
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 6):  # franc
            if (last2 < 39):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==6:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==6:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==6:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 6:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 6:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 6:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
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
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 7):  # spain
            if (last2 < 39):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==7:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==7:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==7:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 7:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 7:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 7:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
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
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 8):  # fizika
            if (last2 < 24):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==8:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==8:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==8:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 8:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 8:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 8:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 9):  # himia
            if (last2 < 29):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==9:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==9:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==9:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 9:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 9:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 9:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 31):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 == 32):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball5)
                elif (last2 == 33):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 == 34):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 10):  # biologia
            if (last2 < 22):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==10:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==10:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==10:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 10:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 10:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 10:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 23):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 11):  # geografia
            if (last2 < 22) or (last2 == 23):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==11:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==11:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==11:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 11:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 11:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 11:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 == 25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball1)
                elif (last2 == 26):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 27):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 28):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 29):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 30):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 31):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 12):
            if (last2 < 17):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==12:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==12:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==12:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 12:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 12:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 12:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 17):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 19):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 20):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 21):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 22):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 == 23):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 24):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                elif (last2 == 25):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball04)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 13):
            if (last2 < 5) or (last2 == 7) or (last2 == 8) or (last2 == 9):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==13:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==13:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==13:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 13:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 13:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 13:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 5):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 6):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball8)
                elif (last2 == 10):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball6)
                elif (last2 == 11):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball8)
                elif (last2 == 12):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball20)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 14):
            if (last2 < 12):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==14:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==14:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==14:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 14:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 14:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 14:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
            else:
                await message.reply('Вот критерии для этого номера:')
                await bot.send_photo(chat_id=message.chat.id, photo=open(
                    'kriterii/' + str(pred) + "/" + last1 + ".png", 'rb'))
                if (last2 == 12):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 13):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 14):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 15):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 16):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 17):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                elif (last2 == 18):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball02)
                elif (last2 == 19):
                    await message.reply('Выберите сколько у вас баллов', reply_markup=kb.ball03)
                cursor.execute(f'UPDATE users SET sost = 7 WHERE id == {tg_id} ')
                db.commit()
        elif (pred == 15):
            if (last2 < 28):
                if any((message.text) == ans[i] for i in range(len(ans))):
                    await  message.reply('Правильно!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1]==15:
                        b[0]+=1
                        b[1]+=1
                        cursor.execute(f'update stat set pred1_prav={b[0]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2]==15:
                        b[2] += 1
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_prav={b[2]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3]==15:
                        b[4] += 1
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_prav={b[4]} where id == {tg_id}')
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
                else:
                    await  message.reply('Ошибка!' + "\n" + "Вот пояснение")
                    await bot.send_photo(chat_id=message.chat.id, photo=open(
                        'predmet/' + str(pred) + "/ans/" + last1 + "/" + str(last2) + ".png", 'rb'))
                    if a[1] == 15:
                        b[1] += 1
                        cursor.execute(f'update stat set pred1_vsego={b[1]} where id == {tg_id}')
                        db.commit()
                    elif a[2] == 15:
                        b[3] += 1
                        cursor.execute(f'update stat set pred2_vsego={b[3]} where id == {tg_id}')
                        db.commit()
                    elif a[3] == 15:
                        b[5] += 1
                        cursor.execute(f'update stat set pred3_vsego={b[5]} where id == {tg_id}')
                        db.commit()
                    cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
                    db.commit()
    elif sost==7:
        cursor.execute(f'UPDATE users SET sost = 2 WHERE id == {tg_id} ')
        db.commit()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
