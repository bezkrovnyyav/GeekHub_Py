# 1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#        Sample data : 1, 5, 7, 23
#        Output :
#        List : [‘1', ' 5', ' 7', ' 23']
#        Tuple : (‘1', ' 5', ' 7', ' 23')

numbers = input('Enter the comma-separated numbers: ')
some_list = list(numbers.split(','))
some_tuple = tuple(some_list)
print('List: ', some_list)
print('Tuple: ', some_tuple)

