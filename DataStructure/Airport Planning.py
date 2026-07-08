import bisect

q, k = map(int, input().split())
data = []

for _ in range(q):
    inp = int(input())
    idx = bisect.bisect_left(data, inp)

    deny = False
    if idx > 0 and inp - data[idx - 1] < k:
        deny = True
    if idx < len(data) and data[idx] - inp < k:
        deny = True

    if deny:
        print("Permission Denied!")
    else:
        bisect.insort(data, inp)
        print("Permission Granted!")

