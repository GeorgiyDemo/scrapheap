class Memes:

    X = int

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.X(self.number)


class SHARAGA:
    def __init__(self):
        self.mas = [[1,] * 3]
        print(self.mas)

    def __check__(self):
        self.mas[0][0] = "KOT"
        print(self.mas)


def main():

    listexample = {}
    obj = Memes(3)
    listexample[Memes] = str(obj.get_number())
    print(listexample)

    zaya = SHARAGA()
    zaya.__check__()


if __name__ == "__main__":
    main()
