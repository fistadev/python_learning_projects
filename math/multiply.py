# calculator multiply

print('We multiply your input numbers using map().')
print('Should be an integer number bigger than 1.')

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def multiply(n, m):
    return n * m

result = multiply(num1, num2)
print(f'If we multiply {num1} by {num2}, the result is: ', result)



# # Return square of n
# def multiply(n, m):
#     return n * m
# # print(multiply(2, 3))
