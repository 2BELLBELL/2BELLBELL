import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
# 보유 머니, 주식 보유량
jun = [n, 0]
sung = [n, 0]

for i in range(len(arr)):
    if jun[0] // arr[i] > 0:
        jun = [jun[0] % arr[i], jun[1] + jun[0] // arr[i]]

    if i > 2 and sung[1] != 0 and arr[i - 3] < arr[i - 2] < arr[i - 1]:
        sung = [sung[0] + arr[i] * sung[1], 0]
    elif i > 2 and arr[i - 3] > arr[i - 2] > arr[i - 1]:
        sung = [sung[0] % arr[i], sung[1] + sung[0] // arr[i]]

jun = jun[0] + jun[1] * arr[-1]
sung = sung[0] + sung[1] * arr[-1]

if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")