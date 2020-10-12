# Основа
class Greater:
    def Great(self, input_str):
        print(input_str)


# Задание параметра через конструктор
class BetterGreater:
    # Это типо конструктор
    def __init__(self, str):
        self.str = str

    def Great(self, newstr):
        print(self.str + " " + newstr)


# Задание параметра через обычную функцию
class MoreBetterGreater:
    def setatr(self, atrib):
        self.argstring = atrib

    # Атрибут класса
    CHECK = "123"

    def getatr(self):
        print(self.CHECK + " " + self.argstring)


def main():
    x = Greater()
    x.Great("meow")

    y = BetterGreater("KOTTT")
    y.Great("MOEWWW")

    z = MoreBetterGreater()
    z.setatr("ТАРАКАН ГЕННАДИЙ")
    z.getatr()


if __name__ == "__main__":
    main()
