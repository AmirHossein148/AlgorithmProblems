n, k = map(int, input().split())
data = list(map(int, input().split()))
final_data = [0 for i in range(n)]

result = []
for i in range(min(data) - (n - 1) * k, max(data) + 1):
    for j in range(n):
        final_data[j] = i + j * k
    result.append(sum(abs(final_data[r] - data[r]) for r in range(n)))

print(min(result))