from itertools import product

n = int(input())

for i in list(product([i for i in range(1, n + 1)], repeat=n)):
    print(' '.join(map(str, i)))
