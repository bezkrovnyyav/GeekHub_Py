'''
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color 
з початковим значенням white і метод для зміни кольору фігури, 
а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових 
розмірів об'єктів при їх створенні
'''

class Figure(object):
    color = 'White'

    def change_color(self, color):
        self.color = color

class Oval(Figure):
    def __init__(self, length=3, width=5):
        self.length = length
        self.width = width


class Square(Figure):
    def __init__(self, side=1):
        self.side = side

obj = Figure()
print(obj.color)

obj.change_color('blue')
print(obj.color)

oval = Oval(3, 2)
oval.change_color('grey')
print(oval.color)

square = Square(2)
square.change_color('red')
print(square.color)
print(square.side)
