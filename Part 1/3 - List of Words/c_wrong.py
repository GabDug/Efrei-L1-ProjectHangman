# find the bigger word of the list following the alphabetical order

l = ["abcdef", "abcdefgh", "abcdefghja"]

max_length = 0
pos = 0

for i in range(len(l)):
    if ''.join(sorted(l[i])) == l[i] and len(l[i]) > max_length:
        max_length = len(l[i])
        pos = i

print(f"Longest word is \"{l[pos]}\" at index {pos}.")