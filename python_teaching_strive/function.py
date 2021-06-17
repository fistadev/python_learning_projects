# list and function together
def numbers():
    a = [7, 4, 6, 2, 150, 9, 5]
    a.sort()
    print(a)
    print('The smallest number is: ', a[0])
    print('The largest number is: ', a[-1])
    return a
numbers()