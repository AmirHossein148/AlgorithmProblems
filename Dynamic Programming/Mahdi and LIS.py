from collections import defaultdict

n = int(input())
d = list(map(int, input().split()))

ja = defaultdict(list)
for i in range(n):
    ja[d[i]].append(i)

a = [0] * n
current_val = 1

for val in sorted(ja.keys()):
    for idx in reversed(ja[val]):
        a[idx] = current_val
        current_val += 1

counts = [len(indices) for indices in ja.values()]
max_f = max(counts) if counts else 0

print(max_f)
print(*(a))
