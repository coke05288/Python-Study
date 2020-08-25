def power_iter(x, n):
    result = 1
    # O(n)
    for i in range(n):
        result *= x

    return result


print(power_iter(2, 3))
