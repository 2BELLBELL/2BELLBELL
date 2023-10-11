def calcal():
    stack = []
    idx = 0
    # 괄호 풀어서 스택에 쌓기
    while idx < len(arr):
        if arr[idx] == '(':
            idx += 1
            tmp = arr[idx:idx + 3]
            stack.append(str(eval(str(''.join(tmp)))))
            idx += 4
        else:
            stack.append(arr[idx])
            idx += 1

    result = []
    idx2 = 0
    # 마지막에 순수 계산
    while idx2 < len(stack):
        result.append(stack[idx2])
        if len(result) == 3:
            tmp = str(eval(str(''.join(result))))
            result.clear()
            result.append(tmp)
        idx2 += 1

    return result[0]


def cal(cnt, l):
    global answer
    answer = max(answer, int(cnt))
    if visited.count(False) < 2:
        return

    for i in range(l, len(arr)):
        if not visited[i] and i != len(arr) - 2 and i != len(arr) - 1:
            visited[i] = True
            if i + 3 < len(arr):
                visited[i + 2] = True
            arr.insert(i + 3, ')')
            arr.insert(i, '(')
            visited.insert(i + 3, True)
            visited.insert(i, True)
            cal(calcal(), i)
            visited.pop(i + 4)
            visited.pop(i)
            arr.pop(i + 4)
            arr.pop(i)
            visited[i] = False
            if i + 3 < len(arr):
                visited[i + 2] = False

N = int(input())
arr = list(input())
visited = [False] * N
for i in range(1, N, 2):
    visited[i] = True

answer = -9999999999999999
cal(-999999999999999, 0)

if N == 1:
    print(arr[0])
else:
    print(answer)