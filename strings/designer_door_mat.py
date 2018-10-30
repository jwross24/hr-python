if __name__ == '__main__':
    N, M = input().split()
    N, M = int(N), int(M)

j_list = []

# Calculate the lines for the mat
for j in range(N // 2):
    coeff = 3*(N // 2 - j)
    dashes = coeff*'-'
    j_list.append(dashes + (2*j+1)*'.|.' + dashes)

design = []

# Add first half of mat
[design.append(line) for line in j_list]

# Add middle line of mat
welcome_coeff = int((M-7)/2)
design.append(welcome_coeff*'-' + 'WELCOME' + welcome_coeff*'-')

# Add second half of mat
j_list.reverse()
[design.append(line) for line in j_list]

[print(line) for line in design]
