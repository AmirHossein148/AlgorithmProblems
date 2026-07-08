from math import ceil

n, m, k = map(int, input().split())

if k > ceil(n/2) * ceil(m/2):
    print(-1)
    exit()

array = [['O']*m for i in range(n)]

if k == 1:
    for row in array:
        print("".join(row))
        exit()

count = 1
row_indices = [i for i in range(0,n,2)]
col_indices = [j for j in range(0,m,2)]
for row in range(n):
    if count == k:
        break
    for col in range(m):
        if count == k:
            break
        if row in row_indices and col in col_indices:
            if row+1 < n:
                array[row+1][col] = 'X'
            if col+1 < m:
                array[row][col+1] = 'X'
            if row+1 < n and col+1 < m:
                array[row+1][col+1] = 'X'
            count += 1

for row in array:
    print("".join(row))
