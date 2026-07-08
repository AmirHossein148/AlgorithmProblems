n = int(input())

index = [0]


def Hanoi(n, from_rod, to_rod, helper_rod):
    if n == 1:
        index[0] += 1
        print(f"{index[0]} {from_rod} {to_rod}")
        return

    Hanoi(n - 1, from_rod, helper_rod, to_rod)

    index[0] += 1
    print(f"{index[0]} {from_rod} {to_rod}")

    Hanoi(n - 1, helper_rod, to_rod, from_rod)


Hanoi(n, 'A', 'B', 'C')
