import math

def primeFactors(n):
    while n % 2 == 0:
        set_of_divisor.add(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            set_of_divisor.add(i)
            n = n // i

    if n > 2:
        set_of_divisor.add(n)


def cost(array, x, y, divisor, best):
    cost_of = 0
    remaining = 0
    for k in array:
        if k % divisor == 0:
            remaining += 1
        elif k % divisor == divisor - 1:
            cost_of += min(x, y)
            remaining += 1
        else:
            cost_of += x
        if cost_of >= best:
            return 10**18
    return cost_of if remaining > 0 else 10**18


n, x, y = map(int, input().split())
data = list(map(int, input().split()))
set_of_divisor = set()
factored = set()

for j in data[:min(70,n)]:
    if j not in factored:
        primeFactors(j)
        factored.add(j)
    if j+1 not in factored:
        primeFactors(j+1)
        factored.add(j+1)


best = 10**18
for divisor in set_of_divisor:
    best = min(best, cost(data, x, y, divisor, best))

print(best)



