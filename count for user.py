# counts for the user, at beginning and ending points and by what interval the user desires

low = int(input("Please enter your beginning number to count: "))
high = int(input("Please enter your ending number to count: "))
interval = int(input("Please enter counting interval: "))

for i in range (low, high, interval):
    print(i)
