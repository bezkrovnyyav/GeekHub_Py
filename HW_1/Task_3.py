#3. Write a script to sum of the first n positive integers.

total_sum = 0
number = int(input("Enter the integers for summing: "))
for element in range(number +1):
    total_sum += element

print(total_sum)