N = int(input())
arr = [0] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    s, num = map(int, input().split())
    # 남자 일 때
    if s == 1:
        # 해당 숫자의 배수만 순회
        for i in range(num, N + 1, num):
            # 1이면 0으로 0이면 1로 교체
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    # 여자 일 때
    else:
        # 현재 위치 스위치 바꾸기
        if arr[num] == 1:
            arr[num] = 0
        else:
            arr[num] = 1
        # 좌우로 대칭 확인하며 바꾸기
        for i in range(1, N + 1):
            # arr 의 범위를 벗어나지 않고, 좌우가 같으면 바꾸기
            if 1 <= num - i and N >= num + i and arr[num - i] == arr[num + i]:
                if arr[num - i] == 1:
                    arr[num - i] = arr[num + i] = 0
                else:
                    arr[num - i] = arr[num + i] = 1
            # 대칭이 아닌 경우 중지
            else:
                break

# 20번째 스위치 출력 후 줄바꿈
for i in range(1, len(arr)):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()