import statistics

n, k = map(int, input().split())
data = list(map(int, input().split()))
final_data = [data[0] + i * k for i in range(n)]

b_data = [data[r] - r*k  for r in range(n)]
b_data.sort()
median = b_data[n // 2] if n % 2 == 1 else b_data[(n - 1) // 2]

final_data = [median + j * k for j in range(n)]


print(sum(abs(int(final_data[i] - data[i])) for i in range(n)))







