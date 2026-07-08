def min_coins(input):
    amount = input["amount"]
    coins = input["coins"]

    coins.sort(reverse=True)

    count = 0
    i = 0
    sum_coin = 0

    while amount >= sum_coin:
        if amount == sum_coin:
            return count
        if i == len(coins):
            return -1

        if (amount - sum_coin) / coins[i] >= 1:
            count += 1
            sum_coin += coins[i]
        else:
            i += 1


print(min_coins({"coins": [1, 2, 3], "amount": 0}))


def find_intervals(input):
    nums = input["nums"]
    target = input["target_sum"]
    n = input["n"]

    prefix = 0
    seen = {0: [-1]}
    result = []

    for i, num in enumerate(nums):
        prefix += num

        if prefix - target in seen:
            for start in seen[prefix - target]:
                result.append(nums[start + 1:i + 1])

        seen.setdefault(prefix, []).append(i)

    result.sort(key=lambda x: len(x))
    return result[:n]


print(find_intervals( {"n": 2, "nums": [10, 20, 10, -10, 5, 5, 5, 5, 10], "target_sum": 15}))

