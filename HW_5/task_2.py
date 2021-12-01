'''
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''
def validation_func(username, password):
    special_symbol =['$', '@', '#', '%', '!', '_', '&', '?']
    if len(username) < 3 :
        raise Exception('Username is too short!')
    elif len(username) > 50:
        raise Exception('Username is too long!')
    elif len(password) < 8:
        raise Exception('Password is too short!')
    elif not any(item.isnumeric() for item in password):
        raise Exception('Password should containe at least one digit!')
    elif not any(item.isalpha() for item in password):
        raise Exception('Password should containe at least one letter!')
    elif not any(item.isupper() for item in password):
        raise Exception('Password should containe at least one uppercase letter!')
    elif not any(item in special_symbol for item in password):
        raise Exception("Password should containe at least one of symbols: '$', '@', '#', '%', '!', '_', '&', '?")
    
    return True
    
    
username = input("Enter username: ")
password = input('Enter password: ')
try:
    validation =  validation_func(username, password)
    print(f'Your credentials are {validation}')

except Exception as err:
    print(err)