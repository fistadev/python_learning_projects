# # Counting a loop
count = 0
print('Before:', count)
for num in [9, 41, 12, 3, 74, 15]:
    count += 1
    print(count, "-", num)
print('After:', count)