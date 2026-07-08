import sys
import bisect

input = sys.stdin.readline

n = int(input())
k = int(input())

start_times = list(map(int, input().split()))
cost = list(map(int, input().split()))

combined = sorted(zip(start_times, cost))
print(combined)
start_times = [x[0] for x in combined]
cost = [x[1] for x in combined]

prefix = [0]
for c in cost:
    prefix.append(prefix[-1] + c)

q = int(input())

for _ in range(q):
    left, right = map(int, input().split())

    L = bisect.bisect_right(start_times, left - k)
    R = bisect.bisect_right(start_times, right)
    
    print(prefix[R] - prefix[L])
