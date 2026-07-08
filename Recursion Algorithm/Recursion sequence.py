import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())


def recursive(n):
    if n == 0:
        return 5
    elif n % 2 == 0:
        return recursive(n - 1) - 21
    elif n % 2 == 1:
        return recursive(n - 1) ** 2


print(recursive(n))