n = int(input())
array = list(map(int, input().split()))

up_down_list = []
equal = []
for i in range(n-1):
    if array[i+1] > array[i]:
        up_down_list.append('U')
    elif array[i] > array[i+1]:
        up_down_list.append('D')
    else:
        equal.append(i)


m = len(up_down_list)
result = []
# No shifting problem
for i in sorted(equal, reverse=True):
    array.pop(i)

start = 0
for i in range(m):
    if up_down_list[i] == 'U':
        result.append(array[i])
        result.append(array[i+1])
        start = i + 1
        break

if start == 0:
    print(0)
    exit()

for i in range(start, m):
    if up_down_list[i] != up_down_list[i-1]:
        result.append(array[i+1])
    else:
        if up_down_list[i] == 'D':
            result[-1] = min(result[-1],array[i+1])
        else:
            result[-1] = max(result[-1], array[i + 1])

print(len(result))




















