'''  
Написати скрипт, який пройдеться по списку, який складається із кортежів,
і замінить для кожного кортежа останнє значення. Список із кортежів можна захардкодити.
Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
Значення, введене користувачем, можна ніяк не конвертувати
(залишити рядком). Кількість елементів в кортежу повинна бути різна.
'''


some_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
replacing_string = input('Enter string for replacing: ')
print([item[:-1] + (replacing_string,) for item in some_tuple])