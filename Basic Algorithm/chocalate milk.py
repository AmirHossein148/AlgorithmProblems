n = int(input())
demand = list(map(int, input().split()))

out_source = 0
in_source = 0

for child in demand:
    if child <= 0:
        in_source -= child
    else:
        if in_source >= child:
            in_source -= child
        else:
            child -= in_source
            in_source = 0
            out_source += child

print(out_source)
