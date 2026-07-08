import sys

string = list(input())
for i in string:
    number = [i for _ in range(int(i))]
    number = ''.join(number)
    print(f'{i}: {number}')

