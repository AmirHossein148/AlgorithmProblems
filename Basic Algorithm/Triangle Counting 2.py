n = int(input())

result = set()
for a in range(1, n//2 +1):
    for b in range(a, n - a):
        c = n - a - b
        if  c>=b and a+b>c and a+c>b and b+c>a:
            result.add((a,b,c))

print(len(result))