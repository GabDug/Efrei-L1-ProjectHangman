import random

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()

    print(words[random.randint(0, len(words)-1)])
