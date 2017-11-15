# replaces a word $w_1$ by a word $w_2$
# TODO CHeck with the teacher if $w_1$ is the variable or the content of the string

l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement"]

for i in range(len(l)):
    l[i] = l[i].replace("$w_1$", "$w_2$")

    print(l)
