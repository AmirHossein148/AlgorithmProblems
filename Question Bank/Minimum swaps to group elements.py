import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

countA = s.count('A')
countB = s.count('B')
countC = s.count('C')

s2 = s + s

prefA = [0] * (2 * n + 1)
prefB = [0] * (2 * n + 1)
prefC = [0] * (2 * n + 1)

for i in range(2 * n):
    prefA[i+1] = prefA[i] + (1 if s2[i] == 'A' else 0)
    prefB[i+1] = prefB[i] + (1 if s2[i] == 'B' else 0)
    prefC[i+1] = prefC[i] + (1 if s2[i] == 'C' else 0)

def get_count(pref, l, r):
    return pref[r] - pref[l]

permutations = [
    ('A','B','C'),
    ('A','C','B'),
    ('B','A','C'),
    ('B','C','A'),
    ('C','A','B'),
    ('C','B','A')
]

answer = n

for p in permutations:
    for start in range(n):
        l1 = start
        r1 = l1 + (countA if p[0]=='A' else countB if p[0]=='B' else countC)

        l2 = r1
        r2 = l2 + (countA if p[1]=='A' else countB if p[1]=='B' else countC)

        l3 = r2
        r3 = l3 + (countA if p[2]=='A' else countB if p[2]=='B' else countC)

        correct1 = (
            get_count(prefA, l1, r1) if p[0]=='A' else
            get_count(prefB, l1, r1) if p[0]=='B' else
            get_count(prefC, l1, r1)
        )

        correct2 = (
            get_count(prefA, l2, r2) if p[1]=='A' else
            get_count(prefB, l2, r2) if p[1]=='B' else
            get_count(prefC, l2, r2)
        )

        correct3 = (
            get_count(prefA, l3, r3) if p[2]=='A' else
            get_count(prefB, l3, r3) if p[2]=='B' else
            get_count(prefC, l3, r3)
        )

        total_correct = correct1 + correct2 + correct3
        misplaced = n - total_correct

        answer = min(answer, misplaced)

print(answer)
