def sum(num_list, n):
    sum_num = 0
    for i in num_list:
        sum_num += i

    return sum_num


if __name__ == "__main__":
    # split() -> default = ' '
    m, n, w, h = map(int, input().split())
    wi = []*m
    dj = []*n

    wi = list(map(int, input().split()))
    dj = list(map(int, input().split()))

    answer = [[]*1 for _ in range(m)]

    map_list = [[0]*n for _ in range(m)]

    # wi와 dj의 각각의 합이 일치하지 않으면, 어차피 불가능하므로 -1 출력
    if sum(wi, m)-sum(dj, n) != 0:
        print(-1)
    else:
        check_w = w
        check_h = h
        i = m
        while i > 0:
            max_index = wi.index(max(wi))
            for j in range(len(dj)):
                if dj[j] > 0 and check_w > 0 and wi[max_index] > 0:
                    check_w -= 1
                    wi[max_index] -= 1
                    dj[j] -= 1
                    map_list[max_index][j] = 1
                else :
                    check_h -= 1
                    if check_h == 0:
                        check_w = w
                        check_h = h
                    continue
            i -= 1

        check_answer = 1

        for i in wi :
            if i > 0 : 
                check_answer = 0

        for j in dj :
            if j > 0 : 
                check_answer = 0   

        if check_answer == 1 : 
            print(1)
            for i in range(m):
                check_start = 1
                for j in range(len(map_list[i])):
                    if map_list[i][j] == 1 and check_start == 1:
                        answer[i].append(j+1) 
                        # print(str(j+1) + " ", end='')
                        check_start -= 1
                    elif map_list[i][j] == 0:
                        check_start = 1
                    else :
                        continue
            answer.sort()
            for i in range(m):
                for j in answer[i]:
                    print(j,end=' ')
                print()

        else:
            print(-1)
