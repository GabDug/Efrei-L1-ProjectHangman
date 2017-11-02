l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement","SALUT"]
l2 = []

word = input("Enter your word? ")

for i in range(len(l)):
    w = l[i]
    if word.lower() == w.lower():
        l2.append(i)

print(f"They are {len(l2)} occurences of {word} at index : {l2}")
