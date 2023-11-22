N, M = map(int, input().split())
group_member = {}
member_group = {}
for _ in range(N):
    group = input()
    number = int(input())
    members = [input() for _ in range(number)]
    group_member[group] = members
    for i in members:
        member_group[i] = group

for _ in range(M):
    q = input()
    quiz = int(input())
    if quiz == 0:
        members = group_member[q]
        members.sort()
        for i in members:
            print(i)
    else:
        print(member_group[q])