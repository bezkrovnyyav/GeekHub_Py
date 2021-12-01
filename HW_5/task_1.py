'''
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і 
   третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
       інакше (<silent> == <False>) - породжується виключення LoginException
'''
class LoginException(Exception):
    pass

def login_func(username, password, silent=False):
    login_list = [{'Andrii':'123'}, {'Kolia':'456'}, {'Miker':'789'}, {'Poll':'qwe'}, {'Rembo':'asd'}]
    if silent:
        if any(item.get(username) == password for item in login_list):
            return True
        else:
            return False
    else:
        raise LoginException('You are not loged in!')


if __name__ == '__main__':
    username = input('Enter username: ')
    password = input('Enter password: ')
    silent = input('Enter silent: ')
    print(f'Your login and password are: {login_func(username, password, silent)}')
