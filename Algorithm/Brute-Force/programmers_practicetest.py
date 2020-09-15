def solution(answers):

    answer = []

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    first_p = 0
    second_p = 0
    third_p = 0

    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            first_p += 1
        if answers[i] == second[i%8]:
            second_p += 1
        if answers[i] == third[i%10]:
            third_p += 1

    temp = [first_p, second_p, third_p]
    max_p = max(temp)

    for i in range(len(temp)) :
        if max_p == temp[i] : 
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))