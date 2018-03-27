# Guess my number
#
# The computer picks a randomnumber between 1 and 100
# The player tries to guess it and the computer lets
"""the player know if the guess is too high, too low
or just right"""

import random

def main():
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    the_number = random.randint(1, 100)
    guess = int(input("Take a guess: "))
    tries = 1


    #guessing loop
    while guess != the_number and tries <= 2:
        if guess > the_number:
            print("Lower ...")
        elif guess < the_number:
            print("Higher ...")
        else:
            print("You guessed it! the number was", the_number)
            print("And it only took you", tries, "tries!\n")
            

        guess = int(input("Take a guess: "))
        tries += 1

    if guess != the_number and tries > 2:
        print("\nYou took too long!")
        print("The number was: ", the_number)


main()
