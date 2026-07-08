q = int(input())
data = [0] * q

for i in range(q):
    data[i] = int(input())

result = [1, 1, 2, 3]

for j in range(4, max(data)):
    a = (result[j - 1] + result[j - 2] + result[j - 3] - result[j - 4]) % (10 ** 9 + 7)
    result.append(a)

for k in range(q):
    print(result[data[k] - 1])