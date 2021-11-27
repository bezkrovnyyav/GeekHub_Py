'''
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
Тобто, функція приймає два аргументи: список і величину зсуву 
(якщо ця величина додатня - пересуваємо з кінця на початок, 
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shift_number = int(input("Input integer number for shift: "))

def func_shift (numbers, shift_number):
    if shift_number > 0:
        for item in range(shift_number):
            numbers.insert(0, numbers.pop())
        return numbers
    else :
        for item in range(-shift_number):
            numbers.append(numbers.pop(0))
        return numbers

if __name__ == '__main__':
    print(func_shift(numbers, shift_number))