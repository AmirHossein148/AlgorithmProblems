import sys
input = sys.stdin.readline

n, m = map(int, input().split())
MOD = 2 * m

events = []
phi = []
slope_of = []

initial_sum = 0
total_slope = 0

for i in range(n):
    pos, d = input().split()
    if pos == 0 and d == 'D':
        d = 'U'
    pos = int(pos)

    if d == 'D':
        pos = 2*m - pos

    phi.append(pos)

    if pos <= m:
        actual = pos
        slope = 1
    else:
        actual = 2*m - pos
        slope = -1

    initial_sum += actual
    total_slope += slope
    slope_of.append(slope)

    t_peak = (m - pos) % MOD
    if t_peak == 0 and pos == 0:
        continue
    events.append((t_peak, i)) # Index use to get slope in the future

    t_valley = (-pos) % MOD
    if t_valley == 0 and pos == 0:
        continue
    events.append((t_valley, i)) # Index use to get slope in the future

events.sort()
#print(f'events : {events}')

current_sum = initial_sum
max_sum = current_sum
prev_time = 0
#print(f'first_max_sum : {max_sum}')

for time, idx in events:
    dt = time - prev_time

    current_sum += total_slope * dt
    #print(f'Current_sum : {current_sum}')
    max_sum = max(max_sum, current_sum)

    # t_peak
    if slope_of[idx] == 1:
        slope_of[idx] = -1
        total_slope -= 2
    # t_valley
    else:
        slope_of[idx] = 1
        total_slope += 2

    prev_time = time

print(max_sum)



