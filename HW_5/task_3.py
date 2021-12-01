'''
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''

login_list = [{'Andrii':'123'}, {'Kolia':'456As!k5'}, {'Miker':'789'}, {'Poll':'qwe'}, {'Rembo':'asdWE12!'}]

def validater(username, password):
    special_symbol =['$', '@', '#', '%', '!', '_', '&', '?']
    if len(username) < 3 :
        raise Exception('Username is too short!')
    elif len(username) > 50:
        raise Exception('Username is too long!')
    elif len(password) < 8:
        raise Exception('Password is too short!')
    elif not any(item.isnumeric() for item in password):
        raise Exception('Password should contain at least one digit!')
    elif not any(item.isalpha() for item in password):
        raise Exception('Password should contain at least one letter!')
    elif not any(item.isupper() for item in password):
        raise Exception('Password should contain at least one uppercase letter!')
    elif not any(item in special_symbol for item in password):
        raise Exception("Password should contain at least one of symbols '$', '@', '#', '%', '!', '_', '&', '?")
    
    return True

for dict in login_list:
    for key in dict:
        print(f'Name: {key}')
        print(f'Password: {dict[key]}')
        try:
            if validater(key, dict[key]):
                print(f'Status: OK')
        except Exception as err:
            print(f'Status: {err}')
        print('-----')