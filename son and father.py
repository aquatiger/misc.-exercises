# user enters a name
# finds name of father from a dictionary

choice = input("""
    Press:
    0 to Quit
    1 to add a son-father pair
    2 to replace a son-father pair
    3 to delete a son-father pair
    4 to check a son-father pair
    5 to check a son-grandfather pair
    """)

# dictionary that has the son as the key and the father as the value
sonFather = {"Michael": ("Jordan", "Jenkins"),
                     "Sid": ("Ceasar", "Brutus"),
                     "Elizabeth": ("George", "George"),
                     "George": ("Washington", "Carver")}

if choice == "0":
    print("\nGoodbye.")
    input("Press enter to exit.")

# add a son:father pair
if choice == "1":
    addSon = input("Who is the son?: ")
    if addSon not in sonFather:
        addFather = input("Who is the father?: ")
        sonFather[addSon] = addFather
    else:
        print("\nThis son already exists.")
        print(sonFather)

# replace a son:father pair
if choice == "2":
    replaceSon = input("Who would you like to replace?: ")
    if replaceSon in sonFather:
        replaceFather = input("Who is the father?: ")
        sonFather[replaceSon] = replaceFather
    else:
        print("This son does not exist in our dictionary. Please try again, perhaps adding it.")
        print(sonFather)

# delete a son:father pair
if choice == "3":
    deleteSon = input("Which son would you like to delete? : ")
    deleteFather = input("Are you sure you want to delete? : ")
    if deleteSon in sonFather and deleteFather == "Y":
        del sonFather[deleteSon]
        print(deleteSon + "is deleted.")
        print(sonFather)
    else:
        print("Goodbye.")
        print(deleteSon, "is not in our dictionary.")

if choice == "4":
    checkSon = input("Whose father would you like to see?: ")
    heritage = sonFather[checkSon]
    father = heritage[0]
    print(checkSon + "\'s father is " + father)
else:
    print("Father is unknown")

if choice == "5":
    checkSon = input("Whose grandfather would you like to see?: ")
    heritage = sonFather[checkSon]
    father = heritage[1]
    print(checkSon + "\'s grandfather is " + father)
else:
    print("Grandfather is unknown")
