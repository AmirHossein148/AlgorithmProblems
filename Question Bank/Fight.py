n = int(input())
people = list(map(int, input().split()))
s = input()

people.sort(reverse=True)

r_people = []
a_people = []

r_people.append(people[0])
idx = 1
while idx < n:
    a_people.extend(people[idx: idx + 2])
    idx += 2

    if idx < n:
        r_people.extend(people[idx: idx + 2])
        idx += 2


def calculate_result(get_list, give_list):
    total_get = sum(get_list)
    total_give = sum(give_list)

    if total_give > total_get:
        return 0, None

    count = 0
    for amount in get_list:
        total_get -= amount
        count += 1
        if total_give > total_get:
            return count, amount
    return count, None


if s == 'romina':
    res_count, last_val = calculate_result(a_people, r_people)
else:
    res_count, last_val = calculate_result(r_people, a_people)

print(f"{res_count}\n{last_val}")