T = int(input()) #TC 입력

for tc in range(1, T+1):
    max_arr = []
    N = int(input())  # 수열의 길이 N
    Data = input()
    arr_num = list(Data)  # 수열
    count = 0

    for i in range(N):
        if arr_num[i] == '1':
           count += 1
           max_arr.append(count)
        else:
            count = 0  # 0으로 초기화시켜주기.
            max_arr.append(count)

    print('#%d %d'%(tc, max(max_arr)))
