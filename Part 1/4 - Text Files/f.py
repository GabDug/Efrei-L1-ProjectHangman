# from a given word w1, get a letter l from the user and search it in the word. If the
# letter exists, the program then displays a word w2 of the same length as w1 where
# w2[i] = _ if w2[i] 6= l and w2[i] = l if w1[i] = l.

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
