n = int(input())
data = list(map(int,input().split()))

data.sort()

if n % 2 == 0:
    mid1 = data[n//2 - 1]
    mid2 = data[n//2]
    result = []

    for M in (mid1, mid2):
        total = sum(abs(x - M) for x in data)
        result.append((M, total))

    best = min(result, key=lambda x: x[1])
    print(f'{best[0]} {best[1]}')


else:
    M = data[n//2]
    total = sum(abs(x - M) for x in data)
    print(f'{M} {total}')