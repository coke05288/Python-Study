temp_triangle = []
check = []


def recur(n, m):
    sum = 0
    if n == 0:
        return temp_triangle[n][m]

    if check[n][m]:
        return temp_triangle[n][m]
    else:
        if m == 0:
            sum = temp_triangle[n][m] + recur(n-1, m)
        elif n == m:
            sum = temp_triangle[n][m] + recur(n-1, m-1)
        else:
            sum = temp_triangle[n][m] + max(recur(n-1, m-1), recur(n-1, m))
        temp_triangle[n][m] = sum
        check[n][m] = True
    return temp_triangle[n][m]


def solution(triangle):
    answer = 0
    global temp_triangle, check

    temp_triangle = list(map(list, triangle))
    check = [[False] * len(temp_triangle) for i in range(len(temp_triangle))]

    for i in range(len(temp_triangle)):
        temp = recur(len(temp_triangle)-1, i)
        if answer < temp:
            answer = temp

    return answer


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    print(solution(triangle))
    print(temp_triangle)
