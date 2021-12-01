'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
    https://docs.python.org/3/library/stdtypes.html#range
'''
def range_func(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

print(f'New created range function: {list(range_func(10,3,-1))}')
print(f'Build-in range funcion for test: {list(range(10, 3,-1))}')