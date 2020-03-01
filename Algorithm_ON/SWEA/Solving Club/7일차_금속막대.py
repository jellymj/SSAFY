import sys
sys.stdin = open('input_3.txt', 'r')

T = int(input())

for tc in range(tc, T+1):
    #pair함수 써볼수있을까나?
    N = int(input())
    nasa_arr = list(map(int, input().split())) #pair함수 쓰려면 어떤 형태로 받아야할까?
    # [(3, 4), (2, 3), (4, 5)] ?
    pair = []
    male_lst = []
    female_lst = []
    result_lst = []
    for i in range(len(nasa_arr)):
        if i%2 == 0:
            male_lst.append(nasa_arr[i])  #[1, 5, 2, 4]
        else:
            female_lst.append(nasa_arr[i]) #[2, 1, 4, 3]
    for male in male_lst:
        for female in female_lst:
            pair.append((male, female)) #[(1, 2), (5, 1), (2, 4), (4, 3)]
    for j in range(N):
        for k in range(N):
            if pair[j][0] not in pair[k][1]:
                result_lst.append(pair[j][0]) #result_lst에 5넣기
    print(result_lst)
                # result_lst.append(pair[j][1]) 
                # result_lst.append(pair[][0])                
        






