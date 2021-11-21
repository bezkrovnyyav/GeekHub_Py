'''
8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник,
з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
'''

quantity_of_keys = int(input("Enter number of dictionary keys: "))

result_dict = {item: item**2 for item in range(quantity_of_keys + 1)}

print(f"Dictionary with square of keys in the value is: {result_dict}")
