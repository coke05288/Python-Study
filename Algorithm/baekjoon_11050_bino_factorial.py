# Factorial(combination fomular)
# Runtime Error O(n)*3

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


n, k = map(int, input().split())

if (n >= 1 and n <= 10) and (k >= 0 and k <= n):
    print(int(factorial(n) / (factorial(k) * factorial(n-k))))
