N = int(input())
dob_num = int(input())
arr = list(map(int, input().split()))
photo = []
dob = []
for i in range(dob_num):
    # 해당 학생이 사진틀에 게시되지 않은 경우
    if arr[i] not in photo:
        # 사진틀이 비어있는 공간이 있는 경우
        if len(photo) < N:
            photo.append(arr[i])
            dob.append(0)
        # 사진틀이 이미 꽉 차있는 경우
        else:
            tmp = dob.index(min(dob))
            photo.pop(tmp)
            dob.pop(tmp)
            photo.append(arr[i])
            dob.append(0)
    # 이미 사진틀에 게시 된 경우 추천수 +1
    else:
        dob[photo.index(arr[i])] += 1

photo.sort()
print(*photo)