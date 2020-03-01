import sys
sys.stdin = open('장훈이.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N:점원 수 / B: 선반 높이
    key_lst = list(map(int, input().split())) #점원 키 리스트
    sum_lst = []
#부분집합 만들기.
    for i in range(1<<N):
        possible_list = []
        for j in range(N+1):
            if i & (1<<j):
                possible_list.append(key_lst[j])
        if sum(possible_list) >= B:
            possible_list == possible_list
            sum_lst.append(sum(possible_list))
    min_key = min(sum_lst)
    print('#%d %d' %(tc, min_key-B))

