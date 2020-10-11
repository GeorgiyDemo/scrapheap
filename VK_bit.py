import datetime
import requests
import schedule
import time
import vk

session = vk.Session(access_token="token1")
admin = vk.Session(access_token="token2")
api = vk.API(session)
human = vk.API(admin)
maingroup = 128947927
maingroup_fix = -128947927


def get_users():
    users = api.groups.getMembers(group_id=maingroup)
    mas = users["users"]
    return mas


def messages():
    if now_time.hour == 6 and now_time.minute == 57:
        time.sleep(180)
        kotiki = get_users()
        for i in range(len(kotiki)):
            try:
                api.messages.send(user_id=kotiki[i], message=message)
                print("Отправили сообщение [id" + str(kotiki[i]) + "]")
            except:
                print("Ошибка отправки [id" + str(kotiki[i]) + "]")


def status():
    human.status.set(
        text="Buy: " + str(buy) + "$ Sell: " + str(sell) + "$", group_id=maingroup
    )
    human.wall.post(owner_id=maingroup_fix, from_group=1, message=message)


# Уведомления в личные сообщения
schedule.every(1).minutes.do(messages)

# Статус группы и стена
schedule.every(2).hours.do(status)

while True:
    # Активация костыля
    schedule.run_pending()

    # Работа с временем/датой
    now_date = datetime.date.today()
    now_time = datetime.datetime.now()
    day = now_date.isoweekday()
    cur_hour = now_time.hour
    cur_minute = now_time.minute
    cur_second = now_time.second
    bb = datetime.date.today()

    # Работа с API блокчейна
    check = requests.get("https://blockchain.info/ru/ticker").json()
    USD = check["USD"]
    buy = USD["buy"]
    sell = USD["sell"]
    message = "Buy: " + str(buy) + "$\nSell: " + str(sell) + "$"

    time.sleep(10)
