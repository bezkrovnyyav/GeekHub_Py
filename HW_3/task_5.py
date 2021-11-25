# 5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" 
# і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z


def comparison_numbers(x, y):
    if x == y:
        print(f'вiдповiдь - {x} дорiвнює {y}')
    elif x > y:
        print(f'вiдповiдь - {x} бiльше {y} на {x - y}')
    else:
        print(f'вiдповiдь - {y} бiльше {x} на {y - x}')


if __name__ == '__main__':
    num_1, num_2 = int(input('Input first number: ')), int(input('Input second number: '))
    comparison_numbers(num_1, num_2)