# 1. Створити цикл від 0 до ... (вводиться користувачем). 
# В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

end_number = int(input('Enter positive integer number: '))

for count_number in range(0, end_number + 1):
    if count_number % 17 == 0:
        print(count_number)