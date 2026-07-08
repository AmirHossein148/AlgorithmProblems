from queue import LifoQueue


def apply_operation(data, MyStack, op):
    if op[0] == 'insert':
        idx, val = int(op[1]) - 1, op[2]
        data.insert(idx, val)
        MyStack.put(('insert', idx, val))

    elif op[0] == 'delete':
        idx = int(op[1]) - 1
        val = data.pop(idx)
        MyStack.put(('delete', idx, val))

    elif op[0] == 'undo':
        if MyStack.qsize() == 0:
            return
        last = MyStack.get()
        if last[0] == 'insert':
            data.pop(last[1])
        elif last[0] == 'delete':
            data.insert(last[1], last[2])


n = int(input())
data = []
MyStack = LifoQueue(maxsize=n)

for _ in range(n):
    parts = input().split()
    apply_operation(data, MyStack, parts)

print(*data, sep='')


