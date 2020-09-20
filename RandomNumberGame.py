import random

print("Random Number Guessing Game")

# random number between -100 to 100
number = random.randint(-100, 100)

# number of chances to be given to the user to guess the number
chances = 0

print("Guess a number (between -100 and 100):")
retry_message = "Please play again!"

# While loop to count the number of chances
while chances < 10:

    # Enter a number between -100 to 9
    guess = int(input())

    # Compare the user entered number with the number to be guessed
    if guess == number:

        print("Congratulation YOU WON!!!")
        print(retry_message)
        break

    # Check if the user input is too low
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    # The user entered input is too high
    else:
        print("Your guess was too high: Guess a number lower than", guess)

        # Increase the value of chance by 1
    chances += 1

if not chances < 10:
    print("YOU LOSE!!! The number is " + str(number) + ".")
    print(retry_message)