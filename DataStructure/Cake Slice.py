import bisect

w, h, q = map(int, input().split())

x_piece = [w]
y_piece = [h]
x_pos = [0, w]
y_pos = [0, h]

for _ in range(q):
    c, i = input().split()
    i = int(i)

    if c == 'H':
        l = bisect.bisect_left(y_pos, i) - 1
        r = bisect.bisect_right(y_pos, i)

        indx = bisect.bisect_left(y_piece, y_pos[r] - y_pos[l])

        del y_piece[indx]

        bisect.insort(y_piece, i - y_pos[l])
        bisect.insort(y_piece, y_pos[r] - i)
        bisect.insort(y_pos, i)

    else:
        l = bisect.bisect_left(x_pos, i) - 1
        r = bisect.bisect_right(x_pos, i)

        indx = bisect.bisect_left(x_piece, x_pos[r] - x_pos[l])

        del x_piece[indx]

        bisect.insort(x_piece, i - x_pos[l])
        bisect.insort(x_piece, x_pos[r] - i)
        bisect.insort(x_pos, i)

    print(x_piece[-1] * y_piece[-1])