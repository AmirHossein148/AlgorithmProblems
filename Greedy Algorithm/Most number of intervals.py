n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x: x[1])
count = 1
j = 0

for i in range(1, n):
    if data[i][0] >= data[j][1]:
        count += 1
        j = i

print(count)
