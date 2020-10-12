import json
import requests

# Можно редачить
shashlik = input("Введи свой id в прилке\n>> ")
while True:
    try:
        #

        #

        r1 = requests.get(
            "http://contentf.com/VkLikes/GetPhotosToLike.php?Limit=20&UserId="
            + shashlik
        )
        hosker = json.loads(r1.text)[0]
        UserId = hosker["UserId"]
        PhotoId = hosker["PhotoId"]
        print(UserId)
        print(PhotoId)

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = "OwnerId=" + UserId + "&PhotoId=" + PhotoId + "&UserId=" + shashlik
        r = requests.post(
            "http://contentf.com/VkLikes/LikedPhoto.php", data=payload, headers=headers
        )
        print(r.text)
    except:
        print("МУР")
