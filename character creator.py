# Character craeator program for role playing

pool = 30

attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}

def menu():
    print("\nYou have", pool, "points")
    print("""
        You can apply them to your Strength, Health, Wisdom, or Dexterity.
        
        Press:
        
        0 to Quit
        1 to apply points to Strength
        2 to apply points to Health
        3 to apply points to Wisdom
        4 to apply points to Dexterity
        5 to apply points from Strength to your pool
        6 to apply points from Health to your pool
        7 to apply points from Wisdom to your pool
        8 to apply points from Dexterity to your pool
        """)

menu()
choice = input("Choice: ")

if choice == "0":
    print("Good-bye.")
    input("\nPress enter to exit.")

if choice != "0":
    if choice == "1":
        strengthChoice = input("How many points would you like to transfer from pool to Strength?: ")
        print(strengthChoice)
        attributes["Strength"] += int(strengthChoice)
        print(attributes.get("Strength"))
        pool -= int(strengthChoice)
        print(pool)

    elif choice == "2":
        healthChoice = input("How many points would you like to transfer from pool to Health?: ")
        print(healthChoice)
        attributes["Health"] += int(healthChoice)
        print(attributes.get("Health"))
        pool -= int(healthChoice)
        print(pool)

    elif choice == "3":
        wisdomChoice = input("How many points would you like to transfer from pool to Wisdom?: ")
        print(wisdomChoice)
        attributes["Wisdom"] += int(wisdomChoice)
        print(attributes.get("Wisdom"))
        pool -= int(wisdomChoice)
        print(pool)

    elif choice == "4":
        dexterityChoice = input("How many points would you like to transfer from pool to Dexterity?: ")
        print(dexterityChoice)
        attributes["Dexterity"] += int(dexterityChoice)
        print(attributes.get("Dexterity"))
        pool -= int(dexterityChoice)
        print(pool)


    elif choice == "5":
        strengthPool = input("How many points would you like to transfer from Strength to Pool?: ")
        print(strengthPool)
        attributes["Strength"] -= int(strengthPool)
        print(attributes.get("Strength"))
        pool += int(strengthPool)
        print(pool)

    elif choice == "6":
        healthPool = input("How many points would you like to transfer from Healthto Pool?: ")
        print(healthPool)
        attributes["Health"] -= int(healthPool)
        print(attributes.get("Health"))
        pool += int(healthPool)
        print(pool)

    elif choice == "7":
        wisdomPool = input("How many points would you like to transfer from Wisdom to Pool?: ")
        print(wisdomPool)
        attributes["Wisdom"] -= int(wisdomPool)
        print(attributes.get("Wisdom"))
        pool += int(wisdomPool)
        print(pool)

    elif choice == "8":
        dexterityPool = input("How many points would you like to transfer from Dexterity to Pool?: ")
        print(dexterityPool)
        attributes["Dexterity"] -= int(dexterityPool)
        print(attributes.get("Dexterity"))
        pool += int(dexterityPool)
        print(pool)

