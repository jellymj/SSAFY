'''
T = int(input())

for i in range(0, T):
    card = list(map(int, input().split()))
    num = 0
    count = 1
    # 리스트 안에서 돌려가면서 가장 많이 나온 카드 찾아내기
    for a in range(0, len(card)): # card list에서 전체 돌기. tc1)0~5
        card.count[a]:


    for b in range(a, len(card)):  #card list에서 방금 전에 뽑은거 제외하고 남은 것 중에서 돌리기
                if card[a] == card[b]: #뽑은 두 장 비교하기
                    count += 1 #비교해서 맞다면 장수 더해주기
print(count)
    # 그 카드의 숫자가 뭔지 찾아내기


T = int(input()) #테스트 케이스 번호
N = 0 #카드 장수
card = list(map(int, input().split())) #불러온 숫자 리스트
count_result = 0
result = 0

count =   #각 숫자들 빈도 카운팅해주기
max_value = max(list(count.values()))
for key in list(count.keys()):
    if count[key] == max_value:
        answer.append



count = 1
top = -1
for i in range(len(l)):
    c = l.count(l[i])
    if c > count:
        count = c

'''

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = input()
    Data = [int(_) for _ in Data]
    cnt_lst = [0]*10

    for i in range(N):
        cnt_lst[Data[i]] += 1

    max_index, max_num = 0, 0
    for i in range(len(cnt_lst)-1,-1,-1):
        if cnt_lst[i] > max_index:
            max_index = cnt_lst[i]
            max_num = i















  #카드 장수가 같을 때는 큰 수를 출력한다.
