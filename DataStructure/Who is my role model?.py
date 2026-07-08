from collections import deque

n = int(input())
A = list(map(int, input().split()))
A = [x - 1 for x in A]  # صفر مبنا کردن

deg = [0] * n
for x in A:
    deg[x] += 1

queue = deque()
for i in range(n):
    if deg[i] == 0:
        queue.append(i)

mark = [False] * n
while queue:
    v = queue.popleft()
    mark[v] = True
    deg[A[v]] -= 1
    if deg[A[v]] == 0:
        queue.append(A[v])

res = [i + 1 for i in range(n) if not mark[i]]

print(len(res))
print(*sorted(res))

