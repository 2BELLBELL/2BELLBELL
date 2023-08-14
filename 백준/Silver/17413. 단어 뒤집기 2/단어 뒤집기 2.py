import sys

S = sys.stdin.readline().rstrip()

stack = []
result = []

cut = ''
for i in S:
    if i == '<':
        result.append(cut)
        cut = '' + i
    elif i == '>':
        cut += i
        result.append(cut)
        cut = ''
    else:
        cut += i

result.append(cut)

for i in result:
    if len(i) > 0:
        if i[0] == '<':
            print(i, end='')
        else:
            lst = i.split()
            re_lst = []
            for j in lst:
                re_lst.append(''.join(reversed(list(j))))
            print(*re_lst, end='')