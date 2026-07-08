n = int(input())
data = list(map(int, input().split()))

for i in range(n):
    p = i
    item = data[p]
    while p > 0 and item < data[p - 1]:
        data[p] = data[p - 1]
        p += -1
    data[p] = item

print(*data, sep=' ')