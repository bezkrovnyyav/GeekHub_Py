'''
 6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник.
Дані можна "захардкодити".
       Sample Dictionary :
       dict_1 = {1:10, 2:20}
       dict_2 = {3:30, 4:40}
       dict_3 = {5:50, 6:60}
       Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
first_dict = {1: "one", 2: "two"}
second_dict = {3: "three", 4: "four"}
third_dict = {5: "five", 6: "six"}
for item in (first_dict, second_dict, third_dict): first_dict.update(item)
print(first_dict)