card_color = set()
card_num = {}
answer = 0
for _ in range(5):
    color, num = list(input().split())
    card_color.add(color)
    if int(num) not in card_num.keys():
        card_num[int(num)] = 1
    else:
        card_num[int(num)] += 1

# 카드가 모두 같은 색일때
if len(card_color) == 1:
    tmp = list(card_num.keys())
    tmp.sort()
    flag = True
    # 모든 숫자가 연속적인지 확인
    for i in range(4):
        if tmp[i] + 1 != tmp[i + 1]:
            flag = False
    # 연속적이면 900점 비연속적이면 600점을 가장 큰 숫자에 더해서 출력
    if flag:
        answer = max(answer, (900 + max(card_num.keys())))
    else:
        answer = max(answer, (600 + max(card_num.keys())))
# 카드색이 하나라도 다를때
else:
    # 4장의 숫자가 같거나 3장/2장이 같을때
    if len(card_num.keys()) == 2:
        result = 0
        for k, v in card_num.items():
            if v == 4:
                result += 800 + k
            elif v == 3:
                result += 700 + 10 * k
            elif v == 2:
                result += k
        answer = max(answer, result)
    # 숫자가 3장이 같을 때
    elif len(card_num.keys()) == 3:
        # 1, 1, 3 인 경우
        if list(sorted(card_num.values())) == [1, 1, 3]:
            result = 0
            for k, v in card_num.items():
                if v == 3:
                    result = 400 + k
                    break
            answer = max(answer, result)
        # 1, 2, 2 인 경우
        else:
            result = 300
            tmp = []
            for k, v in card_num.items():
                if v == 2:
                    tmp.append(k)
            if tmp[0] >= tmp[1]:
                result += (tmp[0] * 10) + tmp[1]
            else:
                result += (tmp[1] * 10) + tmp[0]
            answer = max(answer, result)
    # 겹치는 숫자가 한개 있는 경우
    elif len(card_num.keys()) == 4:
        result = 0
        for k, v in card_num.items():
            if v == 2:
                result = 200 + k
                break
        answer = max(answer, result)
    # 모든 숫자가 전부 다른 경우
    else:
        tmp = list(card_num.keys())
        tmp.sort()
        flag = True
        # 모든 숫자가 연속적인지 확인
        for i in range(4):
            if tmp[i] + 1 != tmp[i + 1]:
                flag = False
        # 모든 숫자가 연속됐다면
        if flag:
            result = 500 + max(card_num.keys())
            answer = max(answer, result)
        # 아니라면
        else:
            result = 100 + max(card_num.keys())
            answer = max(answer, result)

print(answer)