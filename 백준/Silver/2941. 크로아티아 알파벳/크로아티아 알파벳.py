txt = input()

CRO = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in CRO:
    if txt.find(i) >= 0:
        txt = txt.replace(i, '1')


print(len(txt))
