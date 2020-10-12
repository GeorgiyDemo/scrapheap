"""
Удаление всех постов в вк

"""
import time
import vk_api


class MainClass:
    # ID группы
    group_id = -47269406
    # Токен с доступом к wall и groups
    token = "token"

    def __init__(self):
        self.vk = vk_api.VkApi(token=self.token)
        self.remover()

    def remover(self):
        """Получает список постов группы и удаляет их"""
        while True:
            result = self.vk.method(
                "wall.get", {"owner_id": self.group_id, "count": 100}
            )
            if result["count"] == 0:
                print("Больше нет постов!")
                return

            all_items = [post["id"] for post in result["items"]]
            for post in all_items:

                buf_result = self.vk.method(
                    "wall.delete", {"owner_id": self.group_id, "post_id": post}
                )
                if buf_result == 1:
                    print("Удалили пост с id{}".format(post))
                else:
                    print(
                        "Что-то пошло не так при удалении поста с id{}, ответ: {}".format(
                            post, buf_result
                        )
                    )
                time.sleep(0.5)


if __name__ == "__main__":
    MainClass()
