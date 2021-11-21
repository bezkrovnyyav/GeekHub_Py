'''
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
'''

strings_list = ["Print", " ", "approximately ", " ", 11, " ", "elements", " ", "for", " ", "me"]

print(f"Testing list = {strings_list}")
print(f"Concatenated elements: {''.join(map(str,strings_list))}")