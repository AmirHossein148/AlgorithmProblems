def min_subset_diff_recursive(arr, i, S_B, n, total):
    if i == n:
        return abs(total - 2 * S_B)

    include = min_subset_diff_recursive(arr, i + 1, S_B + arr[i], n, total)

    exclude = min_subset_diff_recursive(arr, i + 1, S_B, n, total)

    return min(include, exclude)


n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
print(min_subset_diff_recursive(arr, 0, 0, n, total))

