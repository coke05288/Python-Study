# Recursion
# 68ms

def bino(n, k):
    if n == k or k == 0:
        return 1
    return bino(n-1, k-1) + bino(n-1, k)


n, k = map(int, input().split())

if (n >= 1 and n <= 10) and (k >= 0 and k <= n):
    print(bino(n, k))
