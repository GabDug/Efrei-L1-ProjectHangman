import random

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()

    w1 = words[random.randint(0, len(words) - 1)]

    l = input("Choose a letter: ")

    w2 = ""

    if l in w1:
        for i in range(len(w1)):
            if w1[i] == l:
                w2 += l
            else:
                w2 += "_"

        print(w2)
