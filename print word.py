import random

words = ["hemoglobin", "Aquarius", "jellyfish", "tanzanite", "loyalty", "Queen Elizabeth"]

for word in words:
    word = random.choice(words)
    print(word)
    del word
