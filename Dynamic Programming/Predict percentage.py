def LIS(lessons, percentages, n):
    dp = [1] * n
    paths = [[i] for i in range(n)]

    for i in range(n):
        for j in range(i):
            if percentages[j] < percentages[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    paths[i] = paths[j] + [i]
                elif dp[j] + 1 == dp[i]:
                    # Subject which should be changed
                    current_complement = sorted([lessons[k] for k in range(n) if k not in paths[i]])
                    new_complement = sorted([lessons[k] for k in range(n) if k not in (paths[j] + [i])])
                    if new_complement < current_complement:
                        paths[i] = paths[j] + [i]

    max_len = max(dp)
    best_set = None
    for i in range(n):
        if dp[i] == max_len:
            complement = sorted([lessons[k] for k in range(n) if k not in paths[i]])
            if best_set is None or complement < best_set:
                best_set = complement

    return ' '.join(best_set)


lessons = input().split()
percentages = list(map(int, input().split()))
n = len(lessons)

print(LIS(lessons, percentages, n))