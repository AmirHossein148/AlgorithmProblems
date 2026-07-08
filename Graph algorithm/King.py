import queue

MAXN = 3000 * 1000 + 10

mark = [False] * MAXN
dist = [0] * MAXN

def getNumber(permutation):
    fact = 1
    returnValue = 0
    for i in range(len(permutation)):
        fact *= (i + 1)
        returnValue += fact * permutation[i]
    return returnValue

def bfs(start_permutation):
    my_queue = queue.Queue(maxsize=MAXN)
    my_queue.put(start_permutation)
    dist[getNumber(start_permutation)] = 0
    while not my_queue.empty():
        permutation = my_queue.get()
        mark[getNumber(permutation)] = True
        for x in range(1, len(permutation) + 1):
            changed_permutation = permutation[0:x][::-1] + permutation[x:]
            if not mark[getNumber(changed_permutation)]:
                my_queue.put(changed_permutation)
                dist[getNumber(changed_permutation)] = dist[getNumber(permutation)] + 1
                mark[getNumber(changed_permutation)] = True
    return

n = int(input())
permutation = list(map(int, input().split()))

bfs(permutation)

print(dist[getNumber(range(1, n + 1))])
