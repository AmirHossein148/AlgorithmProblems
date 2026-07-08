n = int(input())
array = []
for i in range(n):
    data = list(map(int, input().split()))
    array.append(data[1:])  # skip the first number (length)

result = 0
mark = [False] * (10 ** 6 + 1)


def backtrack(i):
    global result
    if i == n:
        result += 1
        return
    for num in array[i]:
        if not mark[num]:  # only pick if not used before
            mark[num] = True
            backtrack(i + 1)
            mark[num] = False


backtrack(0)
print(result)

