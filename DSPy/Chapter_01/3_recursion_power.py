# O(math.log(n,2))
def power_recursion(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_recursion(x*x, n//2)
    else:
        return x * power_recursion(x*x, (n-1)//2)


print(power_recursion(2, 3))
