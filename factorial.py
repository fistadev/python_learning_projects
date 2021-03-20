# factorial

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f4


a = int(input('Write a number: '))

result = fact(a)
print('Factorial is: ', result)
