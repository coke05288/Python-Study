# Dynamic Programming

def bino(n, k):
    if n == k or k == 0:
        return 1
    if cache[n][k] != -1:
        return cache[n][k]
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n - 1, k)
        return cache[n][k]


n, k = map(int, input().split())

# cache = [[-1]*(n+1)]*(n+1)
cache = [[-1]*(n+1) for i in range(n+1)]

if (n >= 1 and n <= 10) and (k >= 0 and k <= n):
    print(bino(n, k))
