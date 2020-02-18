# import sys
# sys.stdin = open('input_0218.txt', 'r')
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N, K = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     # print(lst)
#     arr = []
#     arr_1 = [0, 0]
#     arr_2 = [0]
#     count = 0
#     for i in range(N):
#         for j in range(N):
#             while len(arr) != K+2:
#                 arr.append(lst[i][j])
#                 for k in range(1, K+1):
#                     if arr_1.insert(k, 1) in arr:
#                         count += 1
#             while len(arr) != K+1:
#                 arr.append(lst[i][j])
#                 for m in range(1, K+1):
#                     if arr_2.insert(m, 1) in arr:
#                         count += 1
#                     if arr_2.insert(m-1, 1) in arr:
#                         count += 1
#
#     for i in range(N):
#         arr = []
#         count = 0
#         for j in range(N):
#             while len(arr) == K+2:
#                 arr.append(lst[j][i])
#                 for k in range(1, K+1):
#                     if arr == arr_1.insert(k, 1):
#                         count += 1
#             while len(arr) == K+1:
#                 arr.append(lst[j][i])
#                 for m in range(1, K+1):
#                     if arr == arr_2.insert(m, 1):
#                         count += 1
#                     if arr == arr_2.insert(m-1, 1):
#                         count += 1
#     print(count)


import sys
sys.stdin = open("input_0218.txt", "r")

T= int(input())

for t in range(1,T+1) :
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    possible = 0

    for y in range(N) :
        for x in range(N-1) :
            count = 0
            check = 0
            if mat[y][x] == 1 and x + K <= N :       #x위치가 1이고 찾고자 하는 최대 위치가 벽 전까지
                count += 1                          # 1 찾았으니까 count + 1
                for i in range(1,K) :
                    if mat[y][x+i] == 1 :
                        count += 1
                    else :
                        break
                if count == K :
                    if x-1 >= 0 :
                        if mat[y][x-1] == 0 :
                            check += 1
                    else:
                        check += 1
                    if x+K < N :
                        if mat[y][x+K] == 0 :
                            check += 1
                    else :
                        check += 1

                if check == 2 :
                    possible += 1

    for x in range(N) :
        for y in range(N-1) :
            count = 0
            check = 0
            if mat[y][x] == 1 and y + K <= N :       #x위치가 1이고 찾고자 하는 최대 위치가 벽 전까지
                count += 1                          # 1 찾았으니까 count + 1
                for i in range(1,K) :
                    if mat[y+i][x] == 1 :
                        count += 1
                    else :
                        break
                if count == K :
                    if y-1 >= 0 :
                        if mat[y-1][x] == 0 :
                            check += 1
                    else:
                        check += 1
                    if y+K < N :
                        if mat[y+K][x] == 0 :
                            check += 1
                    else :
                        check += 1

                if check == 2 :
                    possible += 1



    print('#{} {}'.format(t,possible))