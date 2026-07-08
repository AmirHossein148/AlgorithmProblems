n = map(int, input())
data = list(map(int, input().split()))

data = sorted(data)
time = 0
count = 0

for i in data:
    if (time + 1) <= i:
        count += 1
        time += 1
    else:
        continue

print(count)
