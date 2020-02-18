# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    count = 0
    check_n = n >> 1 #n/2의 몫을 출력. 홀수일 경우 가운데 수는 탐색할 필요X.
    #가로
    for idy in range(8): #글자 길이만큼 탐색
        for idx in range(8-n+1):
            for check in range(check_n):
                if matrix[idy][idx+check] != matrix[idy][idx + n -1-check]:
                    break
            else:   #해당 숫자n개 만큼 다 비교하고 나서야 카운트 올려야 되서 여기. if문과 else문 같은 줄에 쓰면 break때문에 실행안됨.
                count += 1
    for idx1 in range(8):
        for idy1 in range(9-n):
            for check in range(check_n):
                if matrix[idy1+check][idx1] != matrix[idy1+n-1-check][idx1]:
                    break
            else:
                count += 1
    print('#{}'.format(tc), end = ' ')
    print(count) 


                # for p in range(n): #회문인지 검사
                #     count = 0
                #     if arr[p] == arr[-1-p]:
                #         count += 1
    # print(arr)
    # print(count)

     #세로



    # print('#%d %d' %(tc, count))