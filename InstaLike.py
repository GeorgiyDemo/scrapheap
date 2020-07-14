import json
import requests

shashlik = input('Вставь хеш\n>> ')
i = 0
while True:
    r1 = requests.get('http://www.multiliker.com/service/view/?hash=' + shashlik)
    middle = (json.loads(r1.text))['picture']
    print(middle)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = 'hash=' + shashlik + '&media=' + middle + '&answer=%7B%22status%22%3A%20%22ok%22%7D'
    r = requests.post('http://www.multiliker.com/service/like2/', data=payload, headers=headers)
    print('Status:' + json.loads(r.text)['result'] + '\n' + json.loads(r.text)['message'])
    print('Кол-во балласов: ' + str(json.loads(r.text)['customer']['coins']))
