number = list(input())
count = 0

# 각 다이얼 별 카운트에 더한다
for i in number:
    if i == "A" or i == "B" or i == 'C':
        count += 3
    elif i == "D" or i == "E" or i == "F":
        count += 4
    elif i == "G" or i == "H" or i == "I":
        count += 5
    elif i == "J" or i == "K" or i == "L":
        count += 6
    elif i == "M" or i == "N" or i == "O":
        count += 7
    elif i == "S" or i == "R" or i == "Q" or i == "P":
        count += 8
    elif i == "T" or i == "U" or i == "V":
        count += 9
    elif i == "Z" or i == "Y" or i == "X" or i == "W":
        count += 10

print(count)