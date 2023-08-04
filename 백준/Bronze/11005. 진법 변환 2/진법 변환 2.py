# 진법 변환용 문자열 미리 생성
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
answer = ''


while N != 0:
    # 문자열을 슬라이싱하여 answer에 삽입
    answer += str(system[N % B])  
    N //= B

# 거꾸로 출력
print(answer[::-1])