fibo_list = [0, 1]

# O(n)
def fibonacci(n):
    if n < 2:
        return fibo_list[n]
    else :
        for i in range(2, n+1):
            fibo_list.append(fibo_list[i-2] + fibo_list[i-1])
    
    return fibo_list[n]

print(fibonacci(5))
