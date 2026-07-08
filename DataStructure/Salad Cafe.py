import heapq

expHeap = []  # heap of [expiration date, client id]
stringHeap = []  # heap of [string, client id]

MAX_K = 100010
mark = [0] * MAX_K  # if client with ID has been expired mark[ID] = True
string = [0] * MAX_K  # string of each client
lastClientId = 0  # number of clients

n = int(input())

for currentDay in range(n):
    clients = input().split()
    for i in range(1, len(clients), 2):
        heapq.heappush(stringHeap, [clients[i], lastClientId])
        heapq.heappush(expHeap, [int(clients[i + 1]) + currentDay - 1, lastClientId])
        string[lastClientId] = clients[i]
        lastClientId += 1

    # erase all clients that have expired
    result = []  # list of expired clients
    while expHeap:
        minElement = heapq.heappop(expHeap)
        id = minElement[1]
        if minElement[0] <= currentDay:  # expired
            if not mark[id]:  # if not marked, means we delete him earlier
                result.append(string[id])
            mark[id] = True
        else:  # all exp dates are greater than current day
            heapq.heappush(expHeap, minElement)
            break

    # erase single client with smallest string
    while stringHeap:
        minElement = heapq.heappop(stringHeap)
        id = minElement[1]
        if not mark[id]:
            mark[id] = True
            result.append(string[id])
            break

    result.sort()
    print(" ".join(result))












