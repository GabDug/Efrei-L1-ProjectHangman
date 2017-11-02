with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    w1 = input("w1? ")

    for w2 in words:
        if w1.lower() in w2.lower():
            print(f"{w2}")
