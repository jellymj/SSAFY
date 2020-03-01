T = int(input()) #테스트 케이스
# 부분집합 원소의 수 1 <= N <= 12, 부분 집합의 합 1 <= K <= 100
# 만족시키는 부분집합의 개수 구하기
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Len = len(num)
lst =[]

# 1~12 부분집합 생성

for i in range(1 << Len):  # 부분 집합의 개수  ->  2^12
    sub_lst = []
    for j in range(Len):  # 원소의 수만큼 비트 비교(0~12)
        if (i & (1 << j)):# i의 j번째 비트가 1이면 ?///// 2^6과 2^7 자리가 둘다 1인지. 자리 비교.
            sub_lst.append(num[j])
    lst.append(sub_lst) #부분집합 lst 생성
#테스트 케이스 돌리기
for tc in range(1, T+1):
    N, K = map(int, input().split()) #부분집합 원소의 수 N / 부분집합의 합 K
    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)

    result = 0
    for i in len_lst:
        if sum(i) == K:
            result += 1
    print('#%s %d' % (tc, result))


'''
TC = int(input()) 
num = [1,2,3,4,5,6,7,8,9,10,11,12] 
Len = len(num) #부분집합 구하기 
lst = [] 

for i in range(1<<Len):
    sub_lst = [] 
    for j in range(Len): 
        if i & (1<<j): 
        sub_lst.append(num[j]) 
        lst.append(sub_lst) 

for tc in range(1, TC+1): 
    N, K = map(int, input().split()) #길이 맞는 리스트 구하기 
    len_lst = [] 
    for i in lst: 
        if len(i) == N: 
            len_lst.append(i) #합 일치 유무 확인 
        result = 0 
        for i in len_lst: 
            if sum(i) == K: 
                result += 1 print('#%s %d'%(tc, result))
'''

