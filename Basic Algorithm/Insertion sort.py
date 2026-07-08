n = int(input())
data = list(map(int, input().split()))

for i in range(n - 1):
    min_data = i
    for j in range(i + 1, n):
        if data[j] < data[min_data]:
            min_data = j
    data[i], data[min_data] = data[min_data], data[i]

print(*data, sep=' ')