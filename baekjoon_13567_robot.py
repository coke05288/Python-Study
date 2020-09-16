M, n = list(map(int, input().split()))
commands = []
[i, j] = [0, 0]
dir = [[0,1], [-1,0], [0, -1], [1, 0]] # (동, 남, 서, 북)
tmp_idx = 0

for _ in range(n):
    commands.append(input())

# 정답을 출력할지 -1을 출력할지를 확인하기 위한 변수
check_answer = 1

for command in commands:
    # 맵 밖으로 나갈 경우 조건 추가
    if i >= M or j >= M or i < 0 or j < 0:
        check_answer = -1
        break
    else:
        if command[0] == 'M':
            i += dir[tmp_idx][1]*int(command[5:])
            j += dir[tmp_idx][0]*int(command[5:])
        elif command[5] == '0':
            tmp_idx = (tmp_idx + 4 - 1) % 4
        elif command[5] == '1':
            tmp_idx = (tmp_idx + 1) % 4

# 제일 마지막 명령어를 실행 한 뒤 최종 i, j 값 확인
if check_answer == -1 or i >= M or j >= M or i < 0 or j < 0:
    print(-1)
else : 
    print(i, j)

