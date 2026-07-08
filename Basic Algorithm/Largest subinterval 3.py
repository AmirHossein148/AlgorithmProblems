# Kadane's Algorithm
n = int(input())
data = list(map(int, input().split()))

result = [0] * n
result[0] = data[0]

answer = result[0]

for i in range(1, n):
    result[i] = max(data[i], data[i] + result[i - 1])
'''
for j in range(n):
    answer = max(answer, result[j])
'''
print(max(result))