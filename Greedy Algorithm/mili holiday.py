import sys

def find_min_time(array):
    array = sorted(array, key=lambda x: (x[0], -x[1]))

    solving_time = 0
    inputing_time = 0

    for solve, keyboard in array:
        solving_time += solve
        if solving_time > inputing_time:
            inputing_time = solving_time
        inputing_time += keyboard

    return inputing_time

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = int(input())
    array = list()
    for _ in range(t):
        a, b = map(int, input().split())
        array.append((a,b))
    print(find_min_time(array))