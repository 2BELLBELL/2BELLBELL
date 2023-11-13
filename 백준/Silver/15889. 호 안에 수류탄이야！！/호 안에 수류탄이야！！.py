N = int(input())
arr = list(map(int, input().split()))
if N == 1:
    print('권병장님, 중대장님이 찾으십니다')
    exit()
    
ranges = list(map(int, input().split()))
max_range = 0
for i in range(N - 1):
    max_range = max(max_range, arr[i] + ranges[i])
    if max_range < arr[i + 1]:
        print('엄마 나 전역 늦어질 것 같아')
        exit()

print('권병장님, 중대장님이 찾으십니다')