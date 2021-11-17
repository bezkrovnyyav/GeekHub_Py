'''
2. Write a script to print out a set containing all the colours from color_list_1
which are not present in color_list_2.
'''
color_list_1 = set(["White", "Blue", "Red", "Black"])
color_list_2 = set(["Red", "Blue"])
unique_set_of_color = (color_list_1) - (color_list_2)
print(unique_set_of_color)