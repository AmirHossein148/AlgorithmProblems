n = int(input())
array = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

length = 1
prev_diff = 0
start = None

for i in range(1, n):
    diff = array[i] - array[i - 1]
    if diff > 0:
        prev_diff = '+'
        length += 1
        start = i
        break

if start is None:
    print(1)
    exit()

for j in range(start + 1, n):
    diff = array[j] - array[j - 1]
    if diff == 0:
        continue

    if diff > 0:
        diff = '+'
    else:
        diff = '-'

    if prev_diff != diff:
        length += 1

    prev_diff = diff

print(length)
