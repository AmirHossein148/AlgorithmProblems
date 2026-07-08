n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dp = [[-10 ** 18] * (m) for _ in range(n)]
parent = [[None] * m for _ in range(n)]

dp[n - 1][0] = array[n - 1][0]

for i in range(n - 1, -1, -1):
    for j in range(0, m):
        if i == n - 1 and j == 0:
            continue

        down_val = dp[i + 1][j] if i + 1 < n else -10 ** 18
        left_val = dp[i][j - 1] if j - 1 >= 0 else -10 ** 18

        if down_val >= left_val:
            dp[i][j] = down_val + array[i][j]
            parent[i][j] = 'U'
        else:
            dp[i][j] = left_val + array[i][j]
            parent[i][j] = 'R'

print(dp[0][m - 1])

path = []
i, j = 0, m - 1
while not (i == n - 1 and j == 0):
    move = parent[i][j]
    path.append(move)
    if move == 'U':
        i += 1
    else:
        j -= 1

path.reverse()
print(''.join(path))

'''
x, y = n-1, 0
summax = data[x][y]
str_result = ''

while not (x == 0 and y == m - 1):
    up = data[x - 1][y] if x > 0 else -1e18     
    right = data[x][y + 1] if y < m - 1 else -1e18 

    if right >= up:
        y += 1
        str_result += 'R'
        summax += data[x][y]
    else:
        x -= 1
        str_result += 'U'
        summax += data[x][y]

print(summax)
print(str_result)
'''