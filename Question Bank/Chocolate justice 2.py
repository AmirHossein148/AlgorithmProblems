import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, c = map(float, input().split())

choc = []
total = 0.0

for _ in range(n):
    x1, y1, z1, x2, y2, z2 = map(float, input().split())
    area = (y2 - y1) * (z2 - z1)
    volume = area * (x2 - x1)
    total += volume
    choc.append((x1, x2, area))


unit_volume = total / m


def get_vol(x):
    v = 0.0
    for x1, x2, area in choc:
        if x > x1:
            v += (min(x, x2) - x1) * area
    return v


last_x = 0.0
for i in range(1, m):
    target = i * unit_volume
    low = last_x
    high = a

    while True:
        mid = (low + high) / 2
        value = get_vol(mid)

        if abs(value - target) < 1e-4:
            break

        if value < target:
            low = mid
        else:
            high = mid

    last_x = mid
    print(f"{mid:.18f}")