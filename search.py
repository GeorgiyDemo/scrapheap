# -*- coding: utf-8 -*-
from pytils import numeral
import vk, random, time, datetime, os, json, requests, xlrd
session = vk.Session(access_token='token')
api = vk.API(session)
#кол-во ячеек в таблице
count_range = 15

i=1
book = xlrd.open_workbook("CONF.xlsx")
first_sheet = book.sheet_by_index(0)
while i < count_range:
	string = (first_sheet.cell(i,0).value).split(' ', 2)[0]+" "+(first_sheet.cell(i,0).value).split(' ', 2)[1]
	result = api.users.search(q=string,birth_year="2001")
	#print(string+" кол-во людей: "+str(len(result)-1))
	if (len(result)==2):
		print(result[1]["first_name"]+" "+result[1]["last_name"] + " https://vk.com/id"+str(result[1]["uid"]))
	i = i + 1
	time.sleep(1)