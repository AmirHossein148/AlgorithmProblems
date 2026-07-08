import sys

input = sys.stdin.readline

n, m = map(int, input().split())
piston = []
target = set()
MOD = 2*m
max_area = 0

for _ in range(n):
    pos, move = input().split()
    pos = int(pos)
    if move == 'D':
        pos = 2*m - pos

    piston.append((pos, move))

    t_peak = (m - pos) % MOD
    target.add(t_peak)

#print(f'piston : {piston}')
for time in target:
    max_area = max(max_area, sum(min((piston[j][0] + time) % MOD, MOD - (piston[j][0] + time) % MOD) for j in range(n)))
    #print(f'time : {time} \t max_area : {max_area}')

print(max_area)


