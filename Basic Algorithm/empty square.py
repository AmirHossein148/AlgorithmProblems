a = int(input())
b = int(input())

if b >= a:
    print('Wrong order!')
    exit()
if (a - b) % 2 == 1:
    print('Wrong difference!')
    exit()

write = []
border = (a - b)//2
for i in range(a):
    for j in range(a):
        if border-1 < i < a-border and border-1 < j < a-border:
            write.append(' ')
        else:
            write.append('*')
    print(*write)
    write = []


