import json
import requests
import time

# Можно редачить
RGold = 25
#
i = 0
meow = 0
deadline = (RGold * 2)
shashlik = input('Вставь хеш\n>> ')
while True:
    r1 = requests.get('http://www.morelikes.me/service/view/?hash=' + shashlik)
    middle = (json.loads(r1.text))['usertofollow-id']
    print(middle)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = 'hash=' + shashlik + '&user=' + middle + '&answer=%7B%22status%22%3A%20%22ok%22%2C%20%22friendship_status%22%3A%20%7B%22incoming_request%22%3A%20false%2C%20%22followed_by%22%3A%20false%2C%20%22outgoing_request%22%3A%20false%2C%20%22following%22%3A%20true%2C%20%22blocking%22%3A%20false%2C%20%22is_private%22%3A%20false%7D%7D'
    r = requests.post('http://www.morelikes.me/service/follow/', data=payload, headers=headers)
    print('Status:' + json.loads(r.text)['result'] + '\n' + json.loads(r.text)['message'])
    gold = json.loads(r.text)['customer']['coins']
    print('Кол-во балласов: ' + str(gold))

    if int(gold) >= deadline:
        time.sleep(3)
        if int(gold) >= deadline:
            print('- - - - - - - - - -\nЗаказываем подписоны..\n- - - - - - - - - -')
            hack = requests.get(
                'http://www.morelikes.me/service/campaign/?hash=' + shashlik + '&quantity=' + str(RGold))
            i = i + 1
            print('Статус подписоты: ' + json.loads(hack.text)['result'] + '\n' + json.loads(hack.text)['message'])
            meow = (i * RGold)
            print('*Всего накручено ' + str(meow) + ' подписонов*')
