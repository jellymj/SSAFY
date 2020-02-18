'''
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    lst = []
    for i in range(N-M+1):
        lst.append(sum(Data[i:i+M]))

    print('#%s %d'%(tc, max(lst)-min(lst)))
    '''


import sys
sys.stdin = open('input_4835.txt', 'r')

TC = int(input()) #테스트 케이스 개수 T 주어진다.

for i in range(1, TC+1):
    N, M = map(int, input().split()) #정수의 개수 N과 구간의 개수 M
    lst = list(map(int, input().split()))  #N개의 정수 ai로 이뤄진 리스트. 리스트 인덱스는 N-1
    result = []
    for a in range(0, N-M+1): #리스트 내에서 비교할 횟수는 N-M+1
        result.append(sum(lst[a:a+M])) #구간값만큼 리스트 안에서 검사
    print("#%s %d" %(i, max(result)-min(result))) #최대값-최소값




    
    
    
    
    #각 줄마다 #T 답 출력


















