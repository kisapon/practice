S = 'ab'
J = 'aabbccd'
counter = 0
for i in range (len(S)):
    for j in range (len(J)):
        if S[i] == J[j]:
           counter += 1
print(counter)
