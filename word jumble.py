# Word Jumble, works as far as I know
# copied skeleton from book, but added counting, hints, scoring system
# computer picks random word from a tuple and then jumbles it up
# player has to guess original word


import random

# creates the tuple to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)
correct = word
jumble = ""
count = 0
score = 5

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
Welcome to Word Jumble
  Unscramble the letters to make a word.
  (Press the enter key at the prompt to quit.)
"""
)
print("The jumble is: ", jumble)

guess = input("\nYour guess is:  ")
while guess != correct and guess != "":
    count += 1
    if  count >= 5:
        break
    print("Sorry, that's not it.")
    #do another loop for hinting
    hint = input("Would you like a hint?  ")
    if hint == "yes":
        score -= 1
        print("The word begins with: ", correct[0])
    else:
        guess = input("\nYour guess is:  ")


if guess == correct:
    print("That's it! You guessed correctly!\n")
    print("Your score is: ", score)
    print("Thanks for playing!")

input("\nPress the enter key to exit.")
