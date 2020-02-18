# T = int(input())
#
# # def MxM(M):  #파리채 면적에서의 합 구하는 함수
# #     find_MxM = 0
# #     for a in range(M-1):
# #         for b in range(M-1):
# #             find_MxM += matrix[a][b]
# #     return find_MxM
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # 배열 크기 N*N  / 파리채 크기 M*M
#     matrix = [list(map(int, input().split())) for i in range(N)]
#     # print(matrix)
#
#     final_result = 0
#     result_lst = []
#     max_result = 0
#     for i in range(N-M+1): #0~3까지!!!!!!!!!!!!!!
#         for j in range(N-M+1): #3     첫빠로 바뀜
#             result = 0
#             for k in range(M):  #1
#                 for l in range(M): #1
#                     result += matrix[j+l][i+k]   #3, 4 + 4, 3
#             result_lst.append(result)                                     #4, 3 + 4, 4
#
#     max_result = max(result_lst)
#     # max_result = max(result_lst)
#     print('#%d %d' % (tc, max_result))
#

