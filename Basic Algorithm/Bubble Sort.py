n = int(input())
data = list(map(int, input().split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(' '.join(map(str, data)))
