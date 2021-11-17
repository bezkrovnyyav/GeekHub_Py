# 4. Write a script to concatenate N strings.
number_of_str = int(input('Enter number of strings for concatenation: '))
list_of_str = []
for counter in range(number_of_str):
    str_for_concate = input("Enter string for concatenation: ")
    list_of_str.append(str_for_concate)
print(''.join(list_of_str))