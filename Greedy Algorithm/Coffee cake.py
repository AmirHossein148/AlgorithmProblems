n, k = map(int, input().split())
data = list(map(int, input().split()))

if k==1:
    print(max(data))
if k==2:
    print(min( [min([max(data[:i]) ,max(data[i:])]) for i in range(1,n)] ))
if k>=3:
    print(min(data))