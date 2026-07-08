import sys
from collections import Counter
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    first, last = input().split()
    data.append(first)

print(Counter(data).most_common()[0][1])