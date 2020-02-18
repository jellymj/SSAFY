N = int(input()) #숫자 개수. 개수는 항상 홀수로 주어짐
score_lst = list(map(int, input().split())) #점수 리스트
median = int((N/2)+0.5)-1

score_lst.sort()
print(score_lst[median])



