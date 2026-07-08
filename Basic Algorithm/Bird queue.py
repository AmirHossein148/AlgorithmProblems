import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = list(input().split())

for _ in range(m):
    data = input().split()
    func = data[0]
    name = data[1]

    if func == 'insert':
        array.insert(int(data[2]), name)
    elif func == 'relocate':
        index = array.index(name)
        array.pop(index)
        array.insert(index + int(data[2]), name)
    else:
        array.remove(name)

print(*array)




