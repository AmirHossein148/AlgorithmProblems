import heapq

q = int(input())
data_heap = []
count = 0

for current_day in range(1, q + 1):
    inp = list(map(int, input().split()))
    k = inp[0]
    tasks = inp[1:]

    for t in tasks:
        heapq.heappush(data_heap, t + current_day - 1)

    while data_heap and data_heap[0] < current_day:
        heapq.heappop(data_heap)

    if data_heap:
        heapq.heappop(data_heap)
        count += 1

print(count)


