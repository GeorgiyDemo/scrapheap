# -*- coding: utf-8 -*-
import requests
import time
import vk
from captcha_solver import CaptchaSolver

chat_users_list = [334479550, 257350143]
access_token = ""
antigate_token = ""
session = vk.Session(access_token=access_token)
api = vk.API(session)
APIVersion = 5.73


def requests_image(file_url):
    img_data = requests.get(file_url, verify=False).content
    with open('captcha.jpg', 'wb') as handler:
        handler.write(img_data)


def create_group(chat_title):
    chat_title = "MEOW" + str(chat_title)
    try:
        thischat = api.messages.createChat(user_ids=chat_users_list, title=chat_title, v=APIVersion)
        api.messages.removeChatUser(chat_id=thischat, user_id=334479550, v=APIVersion)

    except Exception as e:
        captcha_sid = vk.exceptions.VkAPIError.captcha_sid.__get__(e)
        captcha_url = vk.exceptions.VkAPIError.captcha_img.__get__(e)
        if (captcha_sid == None) and (captcha_url == None):
            time.sleep(3)
            api.messages.createChat(user_ids=chat_users_list, title=chat_title, v=APIVersion)
        requests_image(captcha_url)
        solver = CaptchaSolver('antigate', api_key=antigate_token)
        raw_data = open('captchaGROUP.jpg', 'rb').read()
        captcha_ready = solver.solve_captcha(raw_data)
        print(captcha_ready)
        api.messages.createChat(user_ids=chat_users_list, title=chat_title, v=APIVersion, captcha_sid=captcha_sid,
                                captcha_key=captcha_ready)


def main():
    inputval = int(input("Введите кол-во групп =>"))
    for i in range(inputval):

        try:
            create_group(i)
            print("Группа №" + str(i) + " создана!")
        except:
            print("Что-то не так")
            time.sleep(10)
        time.sleep(3)


main()
