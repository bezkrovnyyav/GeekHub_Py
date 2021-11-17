'''
6. Write a script to check whether a specified value is contained in a group of values.
      Test Data :
       3 -> [1, 5, 8, 3] : True
       -1 -> (1, 5, 8, 3) : False
'''

specified_value = int(input('Please, input some value: '))
group_of_values = tuple(map(int, input('Input your list of comma-separated numbers: ').split(',')))
print(group_of_values)
print(specified_value in group_of_values)

                      