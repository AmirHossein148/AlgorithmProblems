from collections import Counter
import bisect

n, q = map(int, input().split())
data = list(map(int, input().split()))

data = Counter(data)

sorted_keys = sorted(data)
cumulative = []
total = 0

for key in sorted_keys:
    total += data[key]
    cumulative.append((key, total))


for _ in range(q):
    target = int(input())
    idx = bisect.bisect_left(sorted_keys, target)
    if idx == 0:
        print(0)
    else:
        print(cumulative[idx - 1][1])

