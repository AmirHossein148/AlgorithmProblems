n, v = map(int, input().split())
data = []
for _ in range(n):
    happy, a = map(int, input().split())
    data.append((happy, a, happy / a))

data.sort(key=lambda x: x[2], reverse=True)
happiness = 0

for i in range(n):
    if data[i][1] <= v:
        happiness += data[i][0]
        v -= data[i][1]
    else:
        happiness += (v * data[i][2])
        v -= v

print(happiness)

