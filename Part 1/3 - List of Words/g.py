l = ["Salut", "les", "$w_1$", "Anticonstitutionnellement"]

for i in range(len(l)):
    l[i] = l[i].replace("$w_1$", "$w_2$")

print(l)
