# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.


def elements(some_list):
    unique_elements = {}
    for item in some_list:
        if item in unique_elements.keys():
            new_elem = unique_elements[item]
            unique_elements.pop(item)
            unique_elements[item] = new_elem + 1
        else:
            unique_elements[item] = 1
    print(unique_elements)
    return(unique_elements)
if __name__ == '__main__':
    some_list = [1,2,2,3,4,4,4,4,1,3,1,1,5]
    elements(some_list)