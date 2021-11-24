# 4. Створiть 3 рiзних функцiї (на ваш вибiр). 
# Кожна з цих функцiй повинна повертати якийсь результат. 
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, 
# обробляє повернутий ними результат та також повертає результат. 
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def square_of_first_number(num_1):
    return num_1 ** 2

def square_of_secont_number(num_2):
    return num_2 ** 2

def square_of_third_numbers(num_3):
    return num_3 ** 2

def sum_of_three_numbers(num_1, num_2, num_3):
    result = (square_of_first_number(num_1)) + (square_of_secont_number( num_2)) + (square_of_third_numbers(num_3))
    return result

if __name__ == '__main__':
    num_1 = int(input('Input first number:  ')) 
    num_2 = int(input('Input second number: '))
    num_3 = int(input('Input third number: '))
    print(f'Sum of three numbers is: {sum_of_three_numbers(num_1, num_2, num_3)}')