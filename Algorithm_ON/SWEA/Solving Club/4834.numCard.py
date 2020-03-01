'''

TC = int(input())
for tc in range(1, TC+1):
    N = int(input()) #카드 장수
    Data = input() # 카드 숫자 ai
    Data = [int(_) for _ in Data] # data에 있는 값을 정수로 바꿔서 리스트로 바꿔줌
    cnt_lst = [0]*10 

    for i in range(N):
        cnt_lst[Data[i]] += 1 # [0000000000] => []

    max_index, max_num = 0, 0
    for i in range(len(cnt_lst)-1,-1,-1):
        if cnt_lst[i] > max_index:
            max_index = cnt_lst[i]
            max_num = i

    print('#%s %d %d'%(tc, max_num, max_index))
    '''

import sys
sys.stdin = open('input_4834.txt', 'r')

TC = int(input()) #테스트케이스 개수 T
for tc in range(1, TC+1):
         
    N = int(input()) #카드 장수 N
    #card_lst = list(map(int, input().split())) #N개의 숫자 ai 들어있는 리스트. 근데 왜 오류뜨찌?
    card_lst = input()
    card_lst = [int(_) for _ in card_lst] 
    cnt_lst = [0]*10 #0으로 만들어진 리스트 생성[0000000000]

    for i in range(N): #카드 장수만큼 리스트 검사
        cnt_lst[card_lst[i]] += 1 #카드 리스트에 있는 숫자를 인덱스로 받아서 있으면 1씩 더해줌
    
    max_index, max_num = 0, 0
    for i in range(9, 0, -1): #같은 장수면 큰 수 출력되게.
        if cnt_lst[i] > max_index: #가장 많이 나온 수와 장수 찾기
            max_index = cnt_lst[i] #가장 많이 나온 장수
            max_num = i #가장 많이나온수

    print('#%s %d %d' %(tc, max_num, max_index))


    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다

    
    
    













