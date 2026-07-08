from queue import LifoQueue

arr = input()
result = []

myStack = LifoQueue(maxsize=len(arr))

for i in range(len(arr) - 1, -1, -1):
    if arr[i] == '(' and myStack.qsize() == 0:
        print(-1)
        break
    if arr[i] == ')':
        myStack.put(i + 1)
    elif arr[i] == '(':
        result.append((i + 1, myStack.get()))

else:
    if myStack.qsize() > 0:
        print(-1)
    else:
        result.sort(key=lambda x: x[1])
        for j in result:
            print(*j)


