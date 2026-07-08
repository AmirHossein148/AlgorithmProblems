n, r = map(int, input().split())
price = list(map(int, input().split()))

price.sort()
count = 0
for i in range(n):
    if price[i] < r:
        count += 1
        r -= price[i]
    else:
        break

print(count)

