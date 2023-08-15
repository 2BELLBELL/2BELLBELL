import sys

N = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().strip())

for i in range(N):
    alp = chr(i + 65)
    num = sys.stdin.readline().strip()
    for j in range(len(arr)):
        if arr[j] == alp:
            arr[j] = num

def eval_postfix(arr):
    s = []
    for i in arr:
        if i.isnumeric():
            s.append(int(i))
        elif i != " ":
            n2 = s.pop()
            n1 = s.pop()
            if i == "+":
                res = n1 + n2
            elif i == "-":
                res = n1 - n2
            elif i == "*":
                res = n1 * n2
            else:
                res = n1 / n2
            s.append(res)
    return s[0]

print(f'{eval_postfix(arr):.2f}')