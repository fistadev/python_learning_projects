import random
# print("Something")
# x = input("Get input")
# y = rand(a, b)
# print(random.randint(3, 9))

## High Low Game

secret_number = random.randint(1, 100)
guess_num = 0
num_guesses = 0

while int(guess_num) != int(secret_number):
    # print("Too low")
    guess_num = input("Get input: ")
    num_guesses = num_guesses + 1

    if int(guess_num) > int(secret_number):
        print("Too low")
    elif int(guess_num) < int(secret_number):
        print("Too high")

print("Correct")
print("You guessed it in " + int(num_guesses) + " guesses")


# while x_low < x_high:
