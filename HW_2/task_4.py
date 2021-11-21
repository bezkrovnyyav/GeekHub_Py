''' 
4.  Написати скрипт, який об'єднає три словника в новий.
Початкові словники не повинні змінитись. Дані можна "захардкодити".
'''

first_dict = {
              'name': 'Andrii',
              'surname': 'Bezkrovnyi'
             }
second_dict = {
                'phone': '123456',
                'adress': 'Myronivka'
              }
third_dict = {
              'age': 28,
              'education': 'student'
             }
             
dict_res = first_dict | second_dict | third_dict
print(dict_res)