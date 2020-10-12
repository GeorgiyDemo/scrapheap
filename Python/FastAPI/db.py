import typing
import random
from pydantic import BaseModel
from pydantic import Field


class PhraseInput(BaseModel):
    """Phrase model"""

    author: str = "Anonymous"  # имя автора. Если не передано - используется стандартное значение.
    text: str = Field(
        ..., title="Text", description="Text of phrase", max_length=200
    )  # Текст фразы. Максимальное значение - 200 символов.


class PhraseOutput(PhraseInput):
    id: typing.Optional[int] = None  # ID фразы в нашей базе данных.


class Database:
    """
    Our **fake** database.
    """

    def __init__(self):
        self._items: typing.Dict[int, PhraseOutput] = {}  # id: model

    def get_random(self) -> int:
        # Получение случайной фразы
        return random.choice(self._items.keys())

    def get(self, id: int) -> typing.Optional[PhraseOutput]:
        # Получение фразы по ID
        return self._items.get(id)

    def add(self, phrase: PhraseInput) -> PhraseOutput:
        # Добавление фразы

        id = len(self._items) + 1
        phrase_out = PhraseOutput(id=id, **phrase.dict())
        self._items[phrase_out.id] = phrase_out
        return phrase_out

    def delete(self, id: int) -> typing.Union[typing.NoReturn, None]:
        # Удаление фразы

        if id in self._items:
            del self._items[id]
        else:
            raise ValueError("Phrase doesn't exist")
