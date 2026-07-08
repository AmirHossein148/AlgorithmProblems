n, c = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

for i in range(n):
    c -= min(c, max(0, data[i] - c))

print(c)
