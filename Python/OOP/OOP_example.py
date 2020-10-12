class Rectangle:
    def __init__(self, width):
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError


# Теперь работать с width и height можно так, как будто они являются атрибутами:
rect = Rectangle(10)
print(rect.width)

# Можно не только читать, но и задавать новые значения свойствам: rect.width = 50
rect.height = 70
print(rect.width)
print(rect.height)
# Если вы обратили внимание: в setter’ах этих свойств осуществляется
# проверка входных значений, если значение меньше нуля, то будет выброшено исключение ValueE rect.width = -50
