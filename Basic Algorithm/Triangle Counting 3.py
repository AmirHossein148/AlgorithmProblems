n = int(input())

count = 0
for a in range(1, n//2 + 1):
    low = max(0, n//2 - 2*a + 1)
    high = (n - 3*a) // 2
    if high >= low:
        count += (high - low + 1)

print(count)
