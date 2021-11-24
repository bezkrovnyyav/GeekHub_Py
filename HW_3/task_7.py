# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(first_number, action, second_number):
    result = None

    if action == '+':
        result = first_number + second_number
    elif action == '-':
        result = first_number - second_number
    elif action == '*':
        result = first_number * second_number
    elif action == '/':
        if second_number == 0:
            result = 'Division by zero is not possible!'
        else:
            result = first_number / second_number  

    return result

def get_numbers(number):
    return int(input(f'Enter the {number}: '))

if __name__ == '__main__':
    operation = calculator(
                           get_numbers('first number'),
                           input('Input action [+, -, *, /]: '),
                           get_numbers('second number')
                           )
                           
    print(f'Result of operation is: {operation}')