# Replaces a word $w_1$ by a word $w_2$
# Not sure if $w_1$ is the variable or the content of the string

l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement"]
w_1 = str(input("Word to be replaced: "))
w_2 = str(input("Word that replace it: "))

for i in range(len(l)):
    l[i] = l[i].replace(w_1, w_2)

print(l)
