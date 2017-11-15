# replaces a word $w_1$ by a word $w_2$
# TODO CHeck with the teacher if $w_1$ is the variable or the content of the string

l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement"]
a = str(input("word to replace"))
b = str(input("word that replace"))

for i in range(len(l)):
    l[i] = l[i].replace(a, b)

    print(l)
