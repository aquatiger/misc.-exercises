import random

# start off with empty list
heads = 0
tails = 0
count = 0


for i in range(100):
    count += 1
    toss = random.randint(1, 2)
    if toss == 1:
        heads += 1
    elif toss == 2:
        tails += 1

print(heads)
print(tails)

