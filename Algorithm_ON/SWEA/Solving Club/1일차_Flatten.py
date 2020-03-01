T = 10

for tc in range(1, T+1):
    N = int(input())  #덤프 횟수 인풋
    height_lst = list(map(int, input().split())) #상자 높이 리스트 인풋
    len_height_lst = len(height_lst)

  
    #덤프 횟수 이내에 평탄화 작업
    while N != 0:
        min_idx = height_lst.index(min(height_lst))
        max_idx = height_lst.index(max(height_lst))
        
        N -= 1
        height_lst[min_idx] += 1
        height_lst[max_idx] -= 1

    #작업 후 상자 높이의 최대값 - 최소값
    print('#%d %d' % (tc, (max(height_lst) - min(height_lst))))