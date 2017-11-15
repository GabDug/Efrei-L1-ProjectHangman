# displays the number of words and the number of characters in the file

with open("list.txt", "r", encoding="utf-8") as rawfile:
    text = rawfile.read()
    words = text.split()
    text = text.replace('\n', '').replace('\r', '')
    print(text)
    char = len(text.replace('\n', '').replace('\r', ''))
    print(f"Number of words : {len(words)}\n"
          f"Number of characters : {len(text)}")
