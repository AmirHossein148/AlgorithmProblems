import sys

def solve(array, n, k):
    increase = [None] * n
    increase[0] = array[0] - k
    for i in range(1,n):
        s = max(increase[i-1], array[i]-k)
        if s <= array[i]+k:
            increase[i] = s
        else:
            break

    array.reverse()
    decrease = [None] * n
    decrease[0] = array[0] - k
    for i in range(1, n):
        s = max(decrease[i - 1], array[i] - k)
        if s <= array[i] + k:
            decrease[i] = s
        else:
            break

    for i in range(n):
        if increase[i] is not None and decrease[n - 1 - i] is not None:
            return True
    return False


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    # Binary Search
    low = 0
    high = 10 ** 9
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if solve(array, n, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)