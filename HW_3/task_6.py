'''
"f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
'''
def checking_func(some_str):
    letters = "".join(filter(lambda elem: not elem.isdigit(), some_str))
    numbers = "".join(filter(str.isdigit, some_str))
    new_list = []
    
    if 30 <= len(some_str) <= 50:
        print("Количество буквы:",len(letters), "\n Количество цифр:", len(numbers))
    
    elif 30 > len(some_str):
        for item in numbers:
            item = int(item)
            new_list.append(item)
        print("Сумма чисел:",sum(new_list), "\n Буквенный ряд:", letters)

    elif 50 < len(some_str):
        print("Букви в порядку зростання:", "".join(sorted(letters)))
        print("Числа в порядку зростання:", "".join(sorted(numbers)))
if __name__ == '__main__':
    checking_func("fi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6uk6")
