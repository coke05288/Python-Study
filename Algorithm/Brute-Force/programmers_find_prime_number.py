from itertools import permutations
import math

def isPrime(n):
    k = int(math.sqrt(n))

    if n < 2:
        return False

    for i in range(2, k+1):
        if n % i == 0 :
            return False
    return True
    

def solution(numbers):
    answer = []

    for i in range(1, len(numbers)+1):
        num_list = list(map(''.join, permutations(list(numbers), i)))
        # set도 iterable하다!
        for j in set(num_list):
            if isPrime(int(j)):
                answer.append(int(j))

    return len(set(answer))


print(solution("011"))