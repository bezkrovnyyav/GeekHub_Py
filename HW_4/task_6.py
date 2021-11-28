# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, 
# якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
def operation_for_num():
    num = int(input('Input integer number from -1000 to 1000: '))
    if num > 0:
        num = num ** 2
    elif num < 0:
        num = num + 100
    return num

if __name__ =='__main__':
    print(operation_for_num())
