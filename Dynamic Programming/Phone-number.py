import sys

input = sys.stdin.readline

def solve(length, number):
    dp = [False] * (length + 1)
    nxt = [-1] * (length + 1)

    dp[length] = True

    for i in range(length - 1, -1, -1):
        if number[i] == '0':
            continue

        if i + 2 <= length and dp[i + 2]:
            dp[i] = True
            nxt[i] = i + 2
        elif i + 3 <= length and dp[i + 3]:
            dp[i] = True
            nxt[i] = i + 3

    if not dp[0]:
        return "NO", []

    res = []
    i = 0
    while i < length:
        j = nxt[i]
        res.append(number[i:j])
        i = j

    return "YES", res


q = int(input())
for _ in range(q):
    length = int(input())
    number = input()
    valid, res_list = solve(length, number)
    print(valid)
    if valid == 'YES':
        print(len(res_list))
        for item in res_list:
            print(item)

