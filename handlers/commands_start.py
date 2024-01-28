from aiogram import types
from misc import dp,bot
import asyncio
import random
import datetime
import pytz
from .sqlit import get_caption,reg_user,get_caption2
reg_user(1)
content_id = -1002091292683

link0 = -1001961274740 #Сок

# link1 = -1001628061570
# link2 = -1001756828717 #Доманшка
# link3 = -1001622262140
# link4 = -1001652652655
# link5 = -1001754189943
# link6 = -1001669219428

channels = [link0]


time0 = "6:59" #После ночи
time1 = "8:59" #Перед утренней
time2 = "9:59" #Послеутренней
time3 = "12:59" #Перед дневной
time4 = "13:59" #После дневной
time5 = "16:59" #Перед вечерней
time6 = "17:59" #После вечерней
time7 = "20:59" #Перед ночью



async def posting():
    for chaneel in channels:
            try:
                await bot.copy_message(caption = get_caption()[0][0],from_chat_id=content_id,chat_id= chaneel,message_id = random.randint(2,396 - 1), parse_mode='html')

            except Exception as e:
                print(e)
                try:
                    await bot.copy_message(caption=get_caption()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(2, 396 - 1), parse_mode='html')
                    await bot.copy_message(caption=get_caption2()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(2, 396 - 1), parse_mode='html')
                except: pass

    print('Выложил посты во все каналы. Скрипт спит 30 минут')


def second_time(finish_data):
    hours_f = int(finish_data[0:2]) #Часы финиша
    min_f = int(finish_data[3:]) #Минуты финиша
    second_f = 0

    hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour
    min_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    seconf_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).second


    time_now = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_now,minute = min_now,second = seconf_now)
    time_finish = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_f,minute = min_f,second = second_f)

    delta = (time_finish-time_now).seconds
    return delta



async def sender():
    while True:
        await asyncio.sleep(5)
        hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour

        if  hours_now == 13 or hours_now == 19 or hours_now == 20:
            if hours_now == 13:
                t = second_time("13:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 19:
                t = second_time("19:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 20:
                t = second_time("20:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()


        await asyncio.sleep(1800) #Проверяем каждые 30 минут

