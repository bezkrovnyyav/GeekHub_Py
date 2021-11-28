# 5. Написати функцію < fibonacci >, яка приймає один аргумент 
# і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(some_num):
    list_fibonacci = [0, 1, 1]
    if (some_num>1):
	    while True:
		    if ((list_fibonacci[-1] + list_fibonacci[-2]) > some_num):
			    break
		    else:
			    list_fibonacci.append(list_fibonacci[-1]+list_fibonacci[-2])
	    return list_fibonacci
    return list_fibonacci

if __name__ == '__main__':
    some_num = int(input('Input integer number from zero to 1000: '))
    print(fibonacci(some_num))