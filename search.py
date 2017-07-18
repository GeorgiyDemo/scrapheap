# -*- coding: utf-8 -*-
from pytils import numeral
import vk, random, time, datetime, os, json, requests, xlrd, re
session = vk.Session(access_token='token')
api = vk.API(session)
#кол-во ячеек в таблице
count_range = 8

i=1
book = xlrd.open_workbook("CONF.xlsx")
first_sheet = book.sheet_by_index(0)
while i < count_range:
	string = (first_sheet.cell(i,0).value).split(' ', 2)[0]+" "+(first_sheet.cell(i,0).value).split(' ', 2)[1]
	result = api.users.search(q=string,birth_year="2001")
	print(string+" - людей 2001 года: "+str(len(result)-1))
	if (len(result)==2):
		print(result[1]["first_name"]+" "+result[1]["last_name"] + " https://vk.com/id"+str(result[1]["uid"]))
	else:
		result = api.users.search(q=string,birth_year="2002")
		print(string+" - людей 2002 года: "+str(len(result)-1))
		if (len(result)==2):
			print(result[1]["first_name"]+" "+result[1]["last_name"] + " https://vk.com/id"+str(result[1]["uid"]))

	time.sleep(1)
	result = api.newsfeed.search(q='"'+string+'"')
	if (result[0]!=0) and (result[0]!=1):
		k = 1
		while k < (len(result)):
			if (re.search(string,result[k]["text"]) != None):
				print("--------------\n"+string+"\nСовпадение по новости:\nhttps://vk.com/wall"+str(result[k]["owner_id"])+"_"+str(result[k]["id"]))
			k = k + 1
	i = i + 1
	time.sleep(2)