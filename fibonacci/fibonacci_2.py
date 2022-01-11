# Fibonacci using dinamic programming

# Taking 1st two fibonacci numbers as 0 and 1
FibArray = [0, 1]

n = int(input("Enter a number: "))
 
def fibonacci(n):
   
    # Check is n is less
    # than 0
    if n <= 0:
        print("Incorrect input")
         
    # Check is n is less
    # than len(FibArray)
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib
 
# Driver Program
# print(f'Your Fibonacci number is: ', fib_numbr)
print(fibonacci(n))