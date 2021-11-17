'''
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
'''

decimal_num = input('Enter the comma-separated decimal numbers: ').split(', ')
hexadecimal = map(lambda num: (num, f'0{num}')[len(num) < 2], sorted([hex(int(n))[2:] for n in decimal_num]))
result = ', '.join(hexadecimal)

print(result)