S = list(input())

tmp = []

for i in range(len(S)):
    tmp.append(''.join(S[i:]))

tmp.sort()

for i in tmp:
    print(i)