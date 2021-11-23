# 2. Користувачем вводиться початковий і кінцевий рік. 
# Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).


first_year, last_year = map(int, input('Enter the year interval. Example: 2000 2021: ').split())

for year in range(first_year, last_year + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
