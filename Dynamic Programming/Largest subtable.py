n, m = map(int, input().split())
rows = []

for _ in range(n):
    row = list(map(int, input().split()))
    rows.append(row)

max_sum = float('-inf')

for top in range(n):
    temp = [0] * m

    for bottom in range(top, n):
        for col in range(m):
            temp[col] += rows[bottom][col]

        current_max = temp[0]
        best = temp[0]
        for k in range(1, m):
            current_max = max(temp[k], current_max + temp[k])
            best = max(best, current_max)

        max_sum = max(max_sum, best)

print(max_sum)

'''    
# Check all row slices
for i in range(n):
    for j in range(m):
        for k in range(j + 1, m + 1):
            summax = max(summax, sum(data[i, j:k]))

# Check all column slices
for j in range(m):
    for i in range(n):
        for k in range(i + 1, n + 1):
            summax = max(summax, sum(data[i:k, j]))

print(summax)
'''