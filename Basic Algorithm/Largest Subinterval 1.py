n = int(input())
data = list(map(int, input().split()))

result = []
for i in range(n):
    sum_of_data = 0
    for j in range(i, n):
        sum_of_data += data[j]
        result.append(sum_of_data)

print(max(result))