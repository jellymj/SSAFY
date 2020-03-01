import sys
sys.stdin = open('input_2.txt', 'r')


for tc in range(1, 11):
    T = int(input())
    sum_lst = [] #각 행, 열, 대각선 sum값 넣을 리스트
    num_arr = [list(map(int, input().split()))for i in range(100)]
    daegak_sum_1 = 0
    daegak_sum_2 = 0
    for i in range(100):
        hang_sum = 0
        for j in range(100):
            hang_sum += num_arr[i][j]
        sum_lst.append(hang_sum)
    for k in range(100):
        yul_sum = 0
        for l in range(100):
            yul_sum += num_arr[l][k]
        sum_lst.append(yul_sum)
    for m in range(100):
        daegak_sum_1 += num_arr[m][m]
    sum_lst.append(daegak_sum_1)
    for n in range(100):
        daegak_sum_2 += num_arr[n][99-n]
    sum_lst.append(daegak_sum_2)
    print('#%d %d' %(tc, max(sum_lst)))

    