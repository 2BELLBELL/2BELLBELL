from collections import deque
N = int(input())
arr = list(map(int, input().split()))
stack = deque()
ans = deque()
stack.append(arr.pop())
ans.append(-1)
for i in arr[::-1]:
    if i >= stack[-1]:
        while i >= stack[-1]:
            stack.pop()
            if not stack:
                break
        if stack:
            ans.appendleft(stack[-1])
            stack.append(i)
        else:
            ans.appendleft(-1)
            stack.append(i)
    else:
        ans.appendleft(stack[-1])
        stack.append(i)
print(*ans)