from collections import defaultdict
from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

max_sum = sum(a)

dp = [defaultdict(int) for _ in range(n+1)]
dp[0][0] = 1

for val in a:
    for c in range(n-1, -1, -1):
        for s, cnt in list(dp[c].items()):
            dp[c+1][s+val] += cnt

candidates = []
for count in range(1, n+1):
    for s in dp[count]:
        candidates.append((s, count))  # numerator, denominator

def count_leq(numer, denom):
    total = 0
    for count in range(1, n+1):
        for s, cnt in dp[count].items():
            if s * denom <= numer * count:
                total += cnt
    return total

candidates.sort(key=lambda x: x[0]/x[1])

low, high = 0, len(candidates)-1
answer_numer, answer_denom = 0, 1 # 0

while low <= high:
    mid = (low + high) // 2
    numer, denom = candidates[mid]
    if count_leq(numer, denom) >= k:
        answer_numer, answer_denom = numer, denom
        high = mid - 1
    else:
        low = mid + 1

g = gcd(answer_numer, answer_denom)
print(f"{answer_numer//g}/{answer_denom//g}")






