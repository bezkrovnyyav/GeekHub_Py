# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), 
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

months = {
            (12, 1, 2): 'Winter',
            (3, 4, 5): 'Spring',
            (6, 7, 8): 'Summer',
            (9, 10, 11): 'Autumn',
        }

def season():
    num_of_month = int(input('Enter number of month from 1 to 12): '))
    if num_of_month in range(1, 13):
        for month, year_season in months.items():
            if num_of_month in month:
                print(year_season)
    else:
        print('You should enter number of month from 1 to 12!')
        season()

if __name__ == '__main__':
    season()