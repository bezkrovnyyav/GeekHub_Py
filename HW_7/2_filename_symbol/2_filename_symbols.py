'''
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр
'''

seven_letters_file = "seven_letters.txt"
dig_file = 'big_file.txt'

num_of_characters = int(input('Enter number of letters: '))

def number_of_file(filename, num):
    try:
        with open (filename, 'r', encoding="utf-8") as f:
            file_text = f.read()

            text_lenght = len(file_text)
            if (num + num) >= text_lenght:
                print([file_text[:num], file_text[-num:]])
                raise Exception('Text in file is too small, show only first and last letters!')
            
            center_symbol = text_lenght // 2
            lst = [file_text[:num], file_text[center_symbol : center_symbol+num], file_text[-num:]]

            return f'{lst}\n\n{file_text}'  

    except Exception as err:
        return err
        
if __name__ == '__main__':
    print(number_of_file(dig_file, num_of_characters))