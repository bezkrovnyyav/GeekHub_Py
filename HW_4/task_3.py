# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, 
# і яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(random_num):
    return random_num > 1 and all(random_num % item for item in range(2, random_num))

if __name__ == '__main__':
    random_num = int(input('Input random integer number from zero to 1000: '))
    print(is_prime(random_num))