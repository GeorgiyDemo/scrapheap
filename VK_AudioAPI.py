# Прикидываемся авторизованным приложением Kate Mobile
# И используем приват методы работы с аудио VK, да

import requests
import time
import urllib3
from captcha_solver import CaptchaSolver

urllib3.disable_warnings()

access_token = "VK_TOKEN"
antigate_token = "ANTIGATE_TOKEN"

headers = {
    # Хедеры для работы
    "User-Agent": "KateMobileAndroid/50.1 lite-438 (Android 7.0; SDK 24; arm64-v8a; Xiaomi MI 4S; ru)",
    "Host": "api.vk.com",
}


# Загрузка изображений капчи
def requests_image(file_url):
    img_data = requests.get(file_url, verify=False).content
    with open("captcha.jpg", "wb") as handler:
        handler.write(img_data)


# Ищем аудио по глобальному поиску
def audio_search(access_token, artist):
    global headers
    return requests.get(
        "https://api.vk.com/method/audio.search?access_token="
        + access_token
        + "&count=200&q="
        + artist
        + "&sort=2&v=5.71",
        headers=headers,
        verify=False,
    ).json()["response"]["items"]


# Добавление аудио
def add_audio(access_token, audio_id, owner_id):
    global headers
    response = requests.get(
        "https://api.vk.com/method/audio.add?access_token="
        + access_token
        + "&audio_id="
        + str(audio_id)
        + "&owner_id="
        + str(owner_id)
        + "&v=5.71",
        headers=headers,
        verify=False,
    ).json()
    try:
        print(response["response"])
    except:
        print("****Капча на add_audio****\n" + response["error"]["captcha_img"])
        captcha_sid = response["error"]["captcha_sid"]
        requests_image(response["error"]["captcha_img"])
        solver = CaptchaSolver("antigate", api_key=antigate_token)
        raw_data = open("captcha.jpg", "rb").read()
        captcha_ready = solver.solve_captcha(raw_data)
        print(captcha_ready)
        print("Пробуем..")

        check = requests.get(
            "https://api.vk.com/method/audio.add?access_token="
            + access_token
            + "&audio_id="
            + str(audio_id)
            + "&owner_id="
            + str(owner_id)
            + "&v=5.71&captcha_sid="
            + captcha_sid
            + "&captcha_key="
            + captcha_ready,
            headers=headers,
            verify=False,
        ).json()

        if check["response"] != None:
            print("Все успешно!")


def get_audio(access_token, offset):
    WallAudio = requests.get(
        "https://api.vk.com/method/wall.get?access_token="
        + access_token
        + "&count=100&offset="
        + str(offset * 100)
        + "&owner_id=-33494375&photo_sizes=1&v=5.71",
        headers=headers,
        verify=False,
    ).json()
    try:
        return WallAudio["response"]["items"]
    except:
        print("****Ограничение на get_audio****\n" + WallAudio["error"]["error_msg"])
        time.sleep(2)
        print("Пробуем..")

        check = requests.get(
            "https://api.vk.com/method/wall.get?access_token="
            + access_token
            + "&count=2&offset="
            + str(offset * 2)
            + "&owner_id=-33494375&photo_sizes=1&v=5.71",
            headers=headers,
            verify=False,
        ).json()

        if check["response"] != None:
            print("Все успешно!")

        return check["response"]["items"]


for offset in range(2194):
    GroupAudioList = get_audio(access_token, offset)
    for i in range(len(GroupAudioList)):

        try:

            for attachment in range(len(GroupAudioList[i]["attachments"])):
                if GroupAudioList[i]["attachments"][attachment]["type"] == "audio":
                    ThisAudio = GroupAudioList[i]["attachments"][attachment]["audio"]
                    print(
                        "Добавляем "
                        + ThisAudio["artist"]
                        + "/"
                        + ThisAudio["title"]
                        + " с id "
                        + str(ThisAudio["id"])
                        + " от "
                        + str(ThisAudio["owner_id"])
                    )
                    add_audio(access_token, ThisAudio["id"], ThisAudio["owner_id"])

        except KeyError:
            print("---")
