n, x = map(int, input().split())
data = list(map(int, input().split()))

MOD = 10**9 + 7
result = 0

for i in data:
    result = (result * x + i) % MOD

print(result)
