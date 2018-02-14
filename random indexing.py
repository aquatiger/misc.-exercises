# have the computer randomly index from a string the user's input.
# print the index number and the character of the input.

import random

message = input("Please type in message: ")

indexed = random.randrange(0, len(message))
print(indexed)
print(message[indexed])
