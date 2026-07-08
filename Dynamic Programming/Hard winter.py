def solve():
    k = int(input())
    temp = list(map(int, input().split()))

    sums = []
    current_sum = sum(temp[:k])
    sums.append(current_sum)

    for i in range(1, 4 * k):
        current_sum = current_sum - temp[i - 1] + temp[(i + k - 1) % (4 * k)]
        sums.append(current_sum)

    max_s = max(sums)
    min_s = min(sums)

    is_four_seasons = False
    for i in range(4 * k):
        summer_idx = i
        winter_idx = (i + 2 * k) % (4 * k)

        if sums[summer_idx] == max_s and sums[winter_idx] == min_s:
            is_four_seasons = True
            break

    print("Yes" if is_four_seasons else "No")


T = int(input())
for _ in range(T):
    solve()

