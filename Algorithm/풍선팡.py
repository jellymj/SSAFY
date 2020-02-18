#방법 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    maxV = 0  # 최대값 구하기 위한 변수
    for i in range(N):
        for j in range(M):
            k = arr[i][j]  # 현재 위치의 꽃가루 수
            sum = k  # 꽃가루 누적합 할 변수 :sum
            # 현위치 꽃가루 더함
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]  # 새로운 탐색 구역 계산 / ni = 2+(-1) = 1, nj = 2+(0) = 2
                h = 1  # 탐색 깊이
                while 0 <= ni < N and 0 <= nj < M and h <= k:  # 배열 내부인지
                    sum += arr[ni][nj]
                    ni += di[d]
                    nj += dj[d]
                    h += 1
            # 여기 -> 하나의 좌표에 대해서 누적합 완료
            if maxV < sum:
                maxV = sum
    print('#{} {}'.format(tc, maxV))


#방법 2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]  # N X M 행렬 생성

    dx = [-1, 0, 1, 0]  #위 오른 아래 왼(시계방향)
    dy = [0, 1, 0, -1]

    s_list = []
    for x in range(N):
        for y in range(M):
            s = 0 + matrix[x][y]
            for i in range(1, matrix[x][y] +1):
                for j in range(4):   #위 오른 아래 왼
                    nx = x + dx[j] * i     #새로운 x 좌표
                    ny = y + dy[j] * i     #새로운 y 좌표
                    if (0 <= nx <= N-1) and (0 <= ny <= M-1):
                        s += matrix[nx][ny]
            s_list.append(s)
    #print(s_list, '--- S_list')

    print('#{} {}'.format(tc, max(s_list)))

