'''
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури 
при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
'''

class Figure(object):

    def __init__(self, color='white'):
        self.color = color
 
    def change_color(self, color):
        self.color = color

class Oval(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()


class Square(Figure):
    def __init__(self, side, color):
        self.side = side
        Figure.__init__(self, color)

obj = Figure()
print(obj.color)

obj.change_color('blue')
print(obj.color)

oval = Oval(3, 2)
print(oval.color)
oval.change_color('grey')
print(oval.color)

square = Square(2, 'red')
print(square.color)
