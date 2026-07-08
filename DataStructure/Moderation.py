import heapq

q = int(input())
max_heap = []
min_heap = []

for _ in range(q):
    inp = int(input())
    if not max_heap or inp <= -max_heap[0]:
        heapq.heappush(max_heap, -inp)
    else:
        heapq.heappush(min_heap, inp)

    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])

