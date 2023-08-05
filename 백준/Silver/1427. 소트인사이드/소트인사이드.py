import sys

X = list(sys.stdin.readline().strip())

print(''.join(sorted(X)[::-1]))
