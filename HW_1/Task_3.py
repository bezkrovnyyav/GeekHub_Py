#3. Write a script to sum of the first n positive integers.

total_sum = 0
while True:
    numbers = int(input("Enter the integers for summing (enter zero for stoping): "))
    if numbers <= 0:
        break
    total_sum += numbers

print(total_sum)