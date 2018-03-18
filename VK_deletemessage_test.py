# -*- coding: utf-8 -*-
from pytils import numeral
import vk, random, time, datetime, json, requests

#user_id = 13
user_id = 13
chat_fix = 2000000000+user_id
#Основная конфигурация
session = vk.Session(access_token='token')
api = vk.API(session)
APIVersion = 5.73


check = api.messages.send(chat_id=user_id,message="снова бунд(",v=APIVersion)
print(check)
time.sleep(10)
while True:
	try:
		api.messages.edit(peer_id=chat_fix,message="бунд",message_id=check,v=APIVersion)
		time.sleep(2)
		api.messages.edit(peer_id=chat_fix,message="снова",message_id=check,v=APIVersion)
		time.sleep(2)
		api.messages.edit(peer_id=chat_fix,message="снова бунд(",message_id=check,v=APIVersion)
		time.sleep(2)
	except:
		print("Поймали капчу")
		time.sleep(10)