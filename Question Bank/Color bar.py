n, k = map(int, input().split())
array = list(input().strip())

count = 0
for i in range(1, n):
    if array[i] == array[i-1]:
        count += 1
        array[i] = -1

print(count)