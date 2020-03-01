T = int(input())

for tc in range(1, T+1):
    N = int(input())
    z = 0
    matrix = [[0] * N for a in range(N) ]

    while (z == N**2):     # 1~N**2이 될때까지
        for i in range(N):
            z += 1
            matrix[0][i] = z
        for j in range(N-1): #0, 1
            z += 1
            matrix[j+1][N-1] = z
        for k in range(N-2, 1, -1): # 1, 0
            z += 1
            matrix[N-1][k] = z #1, 0
        for l in range(N)


        # for i in range(N):
        #     for j in range(N):
        #         z += 1
        #         # matrix[i][j] = z
        #         if matrix[i][j] == 0:
        #





    #   0    1    2
    # 0 (1) (2)  (3)
    # 1 (8) (9)  (4)
    # 2 (7) (6)  (5)


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     dal = [[0] * N for _ in range(N)]
#     k = 1
#     x = 0
#     y = -1
#     di = 1
#     leng = N
#     while True:
#         for i in range(leng):
#             y += di
#             dal[x][y] = k
#             k += 1
#         leng -= 1
#         if leng == 0:
#             break
#         for j in range(leng):
#             x += di
#             dal[x][y] = k
#             k += 1
#         di *= -1  # 방향 전환
#
#     print("#{}".format(t))
#     for a in dal:
#         print(" ".join(map(str, a)))
