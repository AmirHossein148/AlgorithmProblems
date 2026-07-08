import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

last_pos = {}
max_gap = defaultdict(int)

for i, val in enumerate(array):
    if val not in last_pos:
        max_gap[val] = i + 1
    else:
        max_gap[val] = max(max_gap[val], i - last_pos[val])
    last_pos[val] = i

for val in last_pos:
    max_gap[val] = max(max_gap[val], n - last_pos[val])

ans = min(max_gap.values())

print(ans)