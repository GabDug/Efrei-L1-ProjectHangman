l = ["Salut", "les", "amis", "Anticonstitutionnellement", "salut", "salutations", "sAlUT"]

word_to_delete = "SALUT"
offset = 0

for i in range(len(l)):
    w = l[i + offset]
    if word_to_delete.lower() == w.lower():
        l.pop(i + offset)
        offset -= 1

print(l)
