from collections import Counter
import sys
import heapq
import math

input = sys.stdin.readline

n, m, k = map(int, input().split())
person_data = {}
order_of_arrival = []
capacity_of_mine = m * (2**m)
best_solver = 2**k

for _ in range(n):
    data = list(map(int, input().split()))
    p_id = data[0]
    person_data[p_id] = data[1:]
    order_of_arrival.append(p_id) # Keep track of the input order

largest_keys = heapq.nlargest(best_solver, person_data.keys(), key=lambda k: len(person_data[k]))

top_questions = []
for p_id in largest_keys:
    top_questions.extend(person_data[p_id])

all_counts = Counter(top_questions)

mili_for_every_question = capacity_of_mine / len(all_counts)

mili_for_question_per_person = {
    q: (mili_for_every_question / count)
    for q, count in all_counts.items()
}

people_prize = []

for p_id in order_of_arrival:
    if p_id in largest_keys and person_data[p_id]:
        total_prize = sum(mili_for_question_per_person.get(q, 0) for q in person_data[p_id])
        people_prize.append(math.ceil(total_prize))
    else:
        people_prize.append(0)

print(*people_prize, sep='\n')
