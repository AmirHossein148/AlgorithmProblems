import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))


data.sort(reverse=True)
purchase = [data[-1]]

if n == 1:
    print(1)
    exit()
elif n == 2:
    if data[0] + data[1] <= x:
        print(2)
        exit()
    else:
        print(1)
        exit()

data = data[:n-1]
while data and purchase[-1] + data[-1] <= x:
    #print(data)
    #print(purchase)
    purchase.append(data.pop())

print(len(purchase))

