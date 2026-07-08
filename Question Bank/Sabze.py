from math import ceil

n, k = map(int, input().split())

array = [False] * n
count = 0

array[0] = True
k -= 1

for i in range(1,n):
    if k == 0:
        break
    if array[i-1] == False:
        array[i] = True
        k -= 1
    elif (n-i) <= k:
        array[i] = True
        k -= 1
        count += 1


print(count)
