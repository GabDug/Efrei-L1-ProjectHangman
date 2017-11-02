l = ["Salut", "les", "amis", "Anticonstitutionnellement"]
max_length = 0
pos = 0

for i in range(len(l)):
    if len(l[i]) > max_length:
        max_length = len(l[i])
        pos = i

print(f"Longest word is \"{l[pos]}\" at index {pos}.")
