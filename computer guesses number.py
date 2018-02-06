#computer guesses number a human thought of

import random

def computer_guess():
    # lower limit not 11
    ll = 1
    # upper limit
    ul = 100

    guess = random.randint(ll, ul)
    print(guess)
    print("Is this guess higher or lower than the number you chose?")
    print("\nPress h for computer to guess a higher number.")
    print("\nPress l for computer to guess a lower number.")
    print("\nOr press c if the computer was correct.")
    
suggestion = input()
computer_guess()

if suggestion != 'c':
    if suggestion == 'h':
        guess = ll       # make the new lower limit the guess that was just made
        print(guess)     # print guess and ll, to see if they match
        print(ll)
        computer_guess() # then run the function again to continue
    if suggestion == 'l':
        guess = ul # make the new upper limit the guess that was just made
        print(guess) # print guess and ul, to see if they match
        print(ul)
        computer_guess() # then run the funtion again to continue
                

if suggestion == 'c':
    print("You are correct. The number is ", guess)
