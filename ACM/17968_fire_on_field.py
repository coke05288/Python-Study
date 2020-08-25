if __name__ == '__main__':

    A_list = [1, 1]

    n = int(input())

    if n >= 2:
        for i in range(2, n+1):
            fire = 1
            A_list.append(0)
            while True:
                A_list[i] = fire
                k = 1
                while True:
                    if i-2*k < 0:
                        break
                    if(A_list[i] - A_list[i-k] == A_list[i-k] - A_list[i-2*k]):
                        break
                    k += 1
                if i-2*k < 0:
                    break
                else:
                    fire += 1

    print(A_list[n])
