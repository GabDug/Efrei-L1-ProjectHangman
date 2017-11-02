with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    words_set = sorted(set(words))
    for w in words_set:
        print(f"{words.count(w)} {w}")