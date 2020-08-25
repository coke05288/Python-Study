def factorial(n):
    sum = 1
    # O(n)
    for i in range(1, n+1):
        sum = sum * i

    return sum


print(factorial(5))
