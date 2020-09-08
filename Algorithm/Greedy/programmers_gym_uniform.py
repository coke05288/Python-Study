def solution(n, lost, reserve):
    answer = 0
    uniform = [1 for _ in range(n)]

    for i in lost:
        uniform[i-1] -= 1
    for i in reserve:
        uniform[i-1] += 1

    for i in range(len(uniform)):
        if uniform[i] == 0:
            if i == 0:
                if uniform[i+1] > 1:
                    uniform[i] += 1
                    uniform[i+1] -= 1
            elif i == len(uniform)-1:
                if uniform[i-1] > 1:
                    uniform[i] += 1
                    uniform[i-1] -= 1
            else:
                if uniform[i+1] > 1:
                    uniform[i] += 1
                    uniform[i+1] -= 1
                elif uniform[i-1] > 1:
                    uniform[i] += 1
                    uniform[i-1] -= 1

    for i in range(len(uniform)):
        if uniform[i] >= 1:
            answer += 1

    return answer


n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
