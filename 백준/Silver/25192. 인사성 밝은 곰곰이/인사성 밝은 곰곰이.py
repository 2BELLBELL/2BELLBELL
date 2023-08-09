N = int(input())
arr = set()
cnt = 0

# 총 채팅 횟수만큼 진행
for _ in range(N):
    # set 인 arr 에 채팅 삽입 
    arr.add(input())
    # 채팅에 ENTER 가 들어가는경우
    if 'ENTER' in arr:
        # ENTER 를 제외한 arr 의 수만큼 cnt 에 더하고 arr 를 초기화한다
        cnt += len(arr) - 1
        arr.clear()

# 반복이 끝나면 현재 arr 의 수만큼 cnt 에 더하고 출력한다
cnt += len(arr)
print(cnt)