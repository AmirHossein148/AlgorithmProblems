import sys

input = sys.stdin.readline

def solve(m, n, a, b):
    table = [[0 * n] * m]
    count, start_a, start_b, i, j = 0, 0, 0, 0, 0

    for i in range(m):
        for j in range(n):
            if j-start_b >= b and i-start_a >= a and table[i][j] != 1:
                table[i:i+b][j:j+a] = 1
                count += 1

 t = int(input())
 for _ in range(t):
     m, n, a, b = map(int, input().split())
     solve(m, n, a, b)