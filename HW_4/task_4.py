# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, 
# і вертатиме список простих чисел всередині цього діапазона.

def prime_list():
    first_num = int(input('Input first integer number from zero to 1000: '))
    last_num = int(input('Input second integer number from zero to 1000: '))

    if first_num > 1000 or first_num < 0 or last_num > 1000 or last_num < 0:
        prime_list()
    elif first_num > last_num:
        print('First number should be less than second number')
        prime_list()
    else:
        prime_nums = []
        for elem in range (first_num, last_num):
            result = elem > 1 and all(elem % item for item in range(2, elem))   
            if result:
                prime_nums.append(elem)
    return prime_nums

if __name__ == '__main__':
    print(prime_list())