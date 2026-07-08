import sys
import bisect

n, k, l = map(int, input().split())
data = list(map(int, input().split()))

pos_to_index = {pos: i for i, pos in enumerate(data)}

beg = 0
result = []

if data[-1] + k < l:
    print(-1)
    sys.exit()

while beg + k < l:
    left = bisect.bisect_right(data, beg)
    right = bisect.bisect_right(data, beg + k)

    candidates = data[left:right]

    if not candidates:
        print(-1)
        sys.exit()

    next_pos = max(candidates)
    beg = next_pos
    result.append(pos_to_index[next_pos] + 1)

print(len(result))
print(*result)