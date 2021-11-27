# Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, 
# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

def square_func(square_side):
    square_perimeter = square_side * 4
    square_area = square_side ** 2
    square_diagonal = (2 * square_side ** 2)**0.5
    result = (square_perimeter, square_area, square_diagonal)

    return result
    
if __name__ == '__main__':
    square_side = int(input('Input the sid eof square: '))
    print(square_func(square_side))