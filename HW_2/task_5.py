'''
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
Словник для роботи захардкодити свій.
               Приклад словника (не використовувати):
               {'a': 1, 'b': 3, 'c': 1, 'd': 5}
               Очікуваний результат:
               {'a': 1, 'b': 3, 'd': 5}
'''
input_dictionary = {'key_1': 123, 'key_2': 456, 'key_3': 123, 'key_4': 789}
unique_dictionary = {}

for keys, values in input_dictionary.items():
    if values not in unique_dictionary.values():
        unique_dictionary[keys] = values

print(f"Result = {unique_dictionary}")