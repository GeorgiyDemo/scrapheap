# -*- coding: utf-8 -*-
import re
import time
import vk
import xlrd

session = vk.Session(access_token='token')
api = vk.API(session)
APIVersion = 5.73
# кол-во ячеек в таблице
count_range = 88

i = 1
book = xlrd.open_workbook("CONF.xlsx")
first_sheet = book.sheet_by_index(0)
while i < count_range:

    string = (first_sheet.cell(i, 0).value).split(' ', 2)[0] + " " + (first_sheet.cell(i, 0).value).split(' ', 2)[1]
    result = api.users.search(q=string, birth_year="2002", v=APIVersion)["items"]
    print(string + " - людей 2002 года: " + str(len(result)))
    if (len(result) == 2):
        print(result[1]["first_name"] + " " + result[1]["last_name"] + " https://vk.com/id" + str(result[1]["id"]))
    else:
        result = api.users.search(q=string, birth_year="2003", v=APIVersion)["items"]
        print(string + " - людей 2003 года: " + str(len(result)))
        if (len(result) == 2):
            print(result[1]["first_name"] + " " + result[1]["last_name"] + " https://vk.com/id" + str(result[1]["id"]))

    time.sleep(1)
    result = api.newsfeed.search(q='"' + string + '"', v=APIVersion)['items']
    if (len(result) != 0):
        k = 1
        while k < (len(result)):
            if (re.search(string, result[k]["text"]) != None):
                # print(result[k]["owner_id"])
                print("--------------\n" + string + "\nСовпадение по новости:\nhttps://vk.com/wall" + str(
                    result[k]["owner_id"]) + "_" + str(result[k]["id"]))
            k = k + 1
    i = i + 1
    time.sleep(2)
