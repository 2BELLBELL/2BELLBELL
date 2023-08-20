import sys

N, K = map(int, sys.stdin.readline().split())
arr = [len(sys.stdin.readline().rstrip()) for _ in range(N)]
dic = {}
best_friends = 0

# N 번 학생까지 실행
for i in range(N):
    # 최대 쌍을 넘었다면 k-1 이전 학생의 수 빼주기
    if i > K:
        dic[arr[i-K-1]] -= 1
    # 딕셔너리에 해당 길이의 숫자를 가진 학생이 있다면 값 + 1, 베프 카운팅
    if dic.get(arr[i]) != None:
        dic[arr[i]] += 1
        best_friends += dic[arr[i]]
    # 해당 길이의 학생이 처음이면 딕셔너리 쌍 생성
    else:
        dic[arr[i]] = 0

print(best_friends)