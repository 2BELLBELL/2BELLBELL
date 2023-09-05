letter = {
        'A': '000000',
        'B': '001111',
        'C': '010011',
        'D': '011100',
        'E': '100110',
        'F': '101001',
        'G': '110101',
        'H': '111010',
}
N = int(input())
pw = input()
result = ''
for i in range(0, 6 * N, 6):
    word = pw[i:i+6]
    code = i
    for k, v in letter.items():
        cnt = 0
        if word[0] == v[0]:
            cnt += 1
        if word[1] == v[1]:
            cnt += 1
        if word[2] == v[2]:
            cnt += 1
        if word[3] == v[3]:
            cnt += 1
        if word[4] == v[4]:
            cnt += 1
        if word[5] == v[5]:
            cnt += 1
        if cnt == 6:
            code = k
            break
        elif cnt == 5:
            code = k
            break
    if code == i:
        print(code // 6 + 1)
        exit()
    else:
        result += code
print(result)