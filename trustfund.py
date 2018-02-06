#Trust fund buddy
#demonstrates a logical error

print(
    """
        Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore
    pennies and use only dollar amounts.

    """
    )

car = float(input("Lamborghini Tune-ups: "))
rent = int(input("Manhattan apartment: "))
jet = int(input("Private jet rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal guru and coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total: ", total)
input ("\n\nPress the enter key to exit.")
