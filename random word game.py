# does not do what I want it to do; not sure why
# user chooses random word from  a tuple
# computer prints out all words in jumbled form
# user is told how many letters are in the chosen word
# user gets only 5 guesses


import random

# creates the tuple to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)
correct = word
jumble = ""
count = 0
score = 5

"""
Welcom to Random Word Game
From the list of scrambled words,
Choose the one the computer chose.
"""
print("The word is ", len(word), "letters long.")
# print(word)

for word in WORDS:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]  * (len(word))

print(jumble)

guess = input("\nYour guess is:  ")
while guess != correct and guess != "":
    print(guess)

if guess == correct:
        print("That's it! You guessed correcntly!\n")
        print("Thanks for playing!")
        
input("\nPress the enter key to exit.")

"""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
"""
