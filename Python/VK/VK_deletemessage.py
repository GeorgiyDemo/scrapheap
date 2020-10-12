# -*- coding: utf-8 -*-
import vk

APIVersion = 5.73
session = vk.Session(access_token="token")
api = vk.API(session)


def EditMessage(message_id):
    new_message = input("Введите новое сообщение для замены -> ")
    if user_id == api.users.get(user_ids=0, v=3.0)[0]["uid"]:
        api.messages.edit(
            peer_id=2000000000 + main_message["items"][0]["chat_id"],
            message=new_message,
            message_id=message_id,
            v=APIVersion,
        )
    else:
        api.messages.edit(
            peer_id=user_id, message=new_message, message_id=message_id, v=APIVersion
        )


def RemoveMessage(message_id):
    if (
        api.messages.delete(message_ids=message_id, delete_for_all=1, v=APIVersion)[
            str(message_id)
        ]
        == 1
    ):
        print("Сообщение успешно удалено")


message_string = input("Введи сообщение для работы с ним:\n")
main_message = api.messages.search(
    q=message_string, preview_length=0, offset=0, count=1, v=APIVersion
)
if main_message["count"] == 0:
    print("Не могу найти сообщение")
    exit()
else:
    message_id = main_message["items"][0]["id"]
    user_id = main_message["items"][0]["user_id"]
    print("\nСообщение найдено, id: " + str(message_id))

flag_id = input("Действия с сообщением:\n1) Удаление для всех\n2) Редактирование\n=> ")

if int(flag_id) == 1:
    RemoveMessage(message_id)

if int(flag_id) == 2:
    EditMessage(message_id)
