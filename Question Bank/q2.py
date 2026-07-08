import sys

input = sys.stdin.readline

n = int(input())
tactic = list(map(int, input().split()))

final_answer = 0
M = -10**18

i = 0
while i < n:
    j = i
    while j + 1 < n and (tactic[j + 1] % 2) == (tactic[i] % 2):
        j += 1

    section = set(tactic[i:j + 1])
    for s in section:
        if s > M:
            final_answer += 1

    M = max(M, max(section))

    i = j + 1

print(final_answer)