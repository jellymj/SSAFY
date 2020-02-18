import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(9)]
    # result_a = 0
    # result_b = 0
    result = 1



    #가로
    for j in range(9):
        lst_3rd = []
        for k in range(9):
            lst_3rd.append(arr[j][k])   #가로 줄 검사
        if sorted(lst_3rd) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = 0
    #if 안맞으면 IsTrue = False, break


    #세로
    for l in range(9):
        lst_4th = []
        for m in range(9):
            lst_4th.append(arr[m][l])  # 세로 줄 검사
            lst_4th.sort()
        if lst_4th != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result = 0
    #사각형
    for p in range(0, 9, 3):
        lst_5th = []
        for a in range(p, p+3):
            for b in range(p, p+3):
                lst_5th.append(arr[a][b])
        lst_5th.sort()
        if lst_5th != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                result = 0
    print('#%d %d' %(tc, result))

# T = int(input())
# for tc in range(1, T + 1):
#     stoku_list = []
#     result = 1
#
#     for _ in range(9):
#         stoku_list.append(list(map(int, input().split())))
#     for i in range(9):
#         y_list = []
#         for j in range(9):
#             y_list.append(stoku_list[j][i])
#         for n in range(1, 10):
#             if n not in y_list:
#                 result = 0
#
#     for i2 in range(9):
#         x_list = []
#         for j2 in range(9):
#             x_list.append(stoku_list[i2][j2])
#         for n2 in range(1, 10):
#             if n2 not in x_list:
#                 result = 0
#
#     for move_y in range(3):  # 격자 이동
#         for move_x in range(3):
#             grid_list = []
#             for smallgird_y in range(3):  # 격자 크기
#                 for smallgird_x in range(3):
#                     grid_list.append(stoku_list[3 * move_y + smallgird_y][
#                                          3 * move_x + smallgird_x])  # 3을 안곱해주면 옆으로 한칸씩 이동하기 때문에, 3을 곱해줘야 함
#             for n3 in range(1, 10):
#                 if n3 not in grid_list:
#                     result = 0
#
#     print('#{} {}'.format(tc, result))