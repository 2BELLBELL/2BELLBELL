import sys
input = sys.stdin.readline
import re

p = re.compile('(100+1+|01)+')
T = int(input())
for _ in range(T):
    string = input().rstrip()
    if p.fullmatch(string):
        print('YES')
    else:
        print('NO')