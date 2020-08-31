# Dynamic Programming
# Runtime Error O(n^2)

def bino(n, k):
    cache = [[-1]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        cache[i][0] = 1
        cache[i][i] = 1
    for i in range(1, n+1):
        for j in range(1, j+1):
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

    return cache[n][k]


n, k = map(int, input().split())


if (n >= 1 and n <= 10) and (k >= 0 and k <= n):
    print(bino(n, k))
