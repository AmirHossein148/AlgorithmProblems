import sys
from collections import defaultdict

input = sys.stdin.readline
score = defaultdict(float)

t = int(input())
for _ in range(t):
    prize, count = map(int, input().split())
    data = [x.strip() for x in input().split(',')]

    if count == 1:
        score[data[0]] += prize
        continue

    for i in range(count):
        score[data[i]] += prize * (count - i - 1) / (count - 1)

for name, value in sorted(score.items(), key=lambda x: x[1], reverse=True):
    print(name)
