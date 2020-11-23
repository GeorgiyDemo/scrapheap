import requests
import os
from dotenv import load_dotenv

load_dotenv()
IAM_TOKEN = os.getenv("IAM_TOKEN", None)
FOLDER_ID = os.getenv("FOLDER_ID", None)

headers = {"Authorization" : "Bearer {}".format(IAM_TOKEN)}
params = {"topic" : "general", "folderId" : FOLDER_ID, "lang" : "ru-RU"}
with open("speech.ogg", "rb") as f:
    data = f.read()

r = requests.post("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize",headers=headers, params=params, data=data)
print(r.text)