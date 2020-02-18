'''
for tc in range(1, 11):
    num = int(input())
    Data = list(map(int, input().split()))
    for i in range(num):
        max_d, min_d= max(Data), min(Data)
        index_max_d = Data.index(max_d)
        index_min_d = Data.index(min_d)
        Data[index_max_d] -= 1
        Data[index_min_d] += 1
    print('#%s %d'%(tc, max(Data)-min(Data)))
    '''
import sys
sys.stdin = open('input.txt', 'r')

TC = 10
for tc in range(1, TC+1):
    num_dump = int(input()) #덤프 횟수
    height_lst = list(map(int, input().split())) #상자 높이 리스트
    
    for i in range(num_dump): #덤프 가능 횟수 내에서 최대값, 최소값은 유동적.
        max_height = max(height_lst) #리스트 내 최대값
        min_height = min(height_lst) #리스트 내 최소값
        idx_max = height_lst.index(max_height) #최대값 인덱스
        idx_min = height_lst.index(min_height) #최소값 인덱스
        height_lst[idx_max] -= 1 # 하향 평준화
        height_lst[idx_min] += 1 # 상향 평준화
        
    print('#%d %d' %(tc, max(height_lst)-min(height_lst)))




    #print(max_height(height_lst))

#for i in range(num_dump):#덤프 가능 횟수 범위 내에서
#덤프 가능 횟수 3
# 1 10 4 8 05 => 정렬 => 1 4 5 8 10 =>
# 최솟값이 두번째 최소값과 같거나 클 때까지 or 최대값이 두번째 최대값과 같거나 작을때까지
#   
#    










