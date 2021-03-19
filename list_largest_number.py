# find the largest number on a list

numbers = [3, 7, 5, 15, 97, 11]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
