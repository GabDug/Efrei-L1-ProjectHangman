# displays all the words in the alphabetical order, each followed by its number of occurrences
# in the file.

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    words_set = sorted(set(words))
    for w in words_set:
        print(f"{words.count(w)} {w}")