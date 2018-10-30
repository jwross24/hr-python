from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    S = str(S).upper()
    k = int(k)

# Create the list of permutations
perms = list(permutations(S, k))

# Extract the characters from the permutations into a string
perm_strings = []
for perm in perms:
    perm_string = ''
    for char in perm:
        perm_string = perm_string + char
    perm_strings.append(perm_string)

# Sort the list of strings and print each string
perm_strings.sort()
[print(string) for string in perm_strings]
