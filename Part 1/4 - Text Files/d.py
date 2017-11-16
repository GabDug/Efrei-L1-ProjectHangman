# get a word w1 from the user and displays all the words w2 in the file having w1 as a
# sub-word.
# Suggested example : set w1 as "able"

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    w1 = input("w1? ")

    for w2 in words:
        if w1.lower() in w2.lower():
            print(f"{w2}")
