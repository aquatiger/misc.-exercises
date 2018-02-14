# create length of message and see if the letter e is in the message

message = input("Please enter a message: ")
print("Your message is " + str(len(message)) + " characters long")
if "e" in message:
    print("The most common letter of the English language is in your message.")
else:
    print("There is no letter \"e\" here")

input("\nPress enter to exit.")
