# Dynamic Programming
# 64ms

def bino(n, k):
    cache = [[-1]*(n+1) for i in range(n+1)]

    for i in range(n+1):
        # 필요한 부분까지만 for 연산
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

    return cache[n][k]


n, k = map(int, input().split())


if (n >= 1 and n <= 10) and (k >= 0 and k <= n):
    print(bino(n, k))
