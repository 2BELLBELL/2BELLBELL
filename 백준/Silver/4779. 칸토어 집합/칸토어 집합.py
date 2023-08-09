try:
    while True:
        N = int(input())
        arr = '-' * 3 ** N

        def cantor(n, arr):
            cut = arr.count('-') // 3
            left = arr[:cut]
            mid = arr[cut:len(arr)-cut].replace('-', ' ')
            right = arr[len(arr)-cut:]


            if cut == 1:
                return left + mid + right
            return cantor(n, left) + mid + cantor(n, right)

        if N == 0:
            print('-')
        else:
            print(cantor(N, arr))
except:
    exit()