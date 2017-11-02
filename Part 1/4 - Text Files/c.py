with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    text = text.upper()
    print(text)

    with open("list_upper.txt","w",encoding="utf-8") as rawfile_upper:
        rawfile_upper.write(text)