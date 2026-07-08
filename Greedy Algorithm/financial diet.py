def solve(k, j, p_k, p_j, p_mix):
    def cost(a):
        b = max(0, (k - a + 1)//2)
        c = max(0, (j - a + 1)//2)
        return a * p_mix + b * p_k + c * p_j

    candidates = [0, 1, k, max(0,k-1), j, max(0,j-1), max(k,j)]
    return min(cost(a) for a in candidates)

t = int(input())
for _ in range(t):
    k, j = map(int, input().split())
    p_k, p_j, p_mix = map(int, input().split())
    print(solve(k, j, p_k, p_j, p_mix))