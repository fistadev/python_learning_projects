# workin with map function
  
# Return square of n
def square(n):
    return n ** 2
  
# We square all numbers using map() and the user input

print('We square all numbers using map() and the your input.')
print('Should be a number bigger than 1.')

numbers = ()
user_input = input("Enter a number: ")

for i in range(1, int(user_input) + 1):
    numbers += (i,)

result = map(square, numbers)

print(f'The squares from 1 to {user_input} are: ', list(result))
