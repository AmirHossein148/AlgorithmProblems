n, k = map(int, input().split())
fruits = []
for _ in range(n):
    b, a = map(int, input().split())
    fruits.append((b, a))

fruits.sort(key=lambda x: x[0])

for b, a in fruits:
    if k >= b and a > b:
        k += (a - b)
print(k)

