#성별
#받은 수

num_sw = int(input()) #스위치 개수
pre_sw = list(map(int, input().split())) #스위치 상태 출력.
num_stu = int(input()) #학생 수
sex_num = [list(map(int, input().split())) for i in range(num_stu)] #성별 받은 수

#남자일 때 : 스위치 번호가 자기가 받은 수의 배수이면 스위치 상태 바꿈  (0 1 1 1 0 1 0 1)

for i in range(num_stu):
    if sex_num[i][0] == 1:                    # 남자이면
        for j in range(1, num_sw+1):               #스위치 개수 안에서 돌림
            if j % (sex_num[i][1]) == 0:        #뽑은 숫자가 스위치 번호의 배수일때
                pre_sw[j-1] = 1 - pre_sw[j-1]       #1이면 0을, 0이면 1을 출력

            #else:  # 배수가 아닐 때
            #    pass


    if sex_num[i][0] == 2:                            #여자이면
        count = 0                                    # pre_sw[(sex_num[i][1])-1]  :   자기가 받은 수와 같은 번호가 붙은 스위치
        for k in range(1, (min((num_sw - (sex_num[i][1])), ((sex_num[i][1])-1) ))+1): #최소 구간 지정
            if (pre_sw[(sex_num[i][1])-1+k] == pre_sw[(sex_num[i][1])-1-k]):                         #좌우 일치 비교
                count = k        #좌우 대칭 스위치 구간 길이
            else:
                break

            #else:
            #    break         받은 수 3  count = 2   0,5 = 0, 1, 2, 3, 4
        for a in range((sex_num[i][1]) - 1 - count, (sex_num[i][1]) - 1 + count+1):  # 해당 구간에 해당하는 스위치는
                    pre_sw[a] = 1 - pre_sw[a]  # 속한 스위치의 상태를 모두 바꾼다.

#print('%s' % (pre_sw[:20:]), sep=' ', end='\n')
lst = list(map(str, pre_sw))
for i in range(len(lst)):
    if i%20 == 0 and i!=0:
        print()
    print(' '.join(lst[i]), end=' ')











#여자일 때
 #자기가 받은 수와 같은 번호가 붙은 스위치 중심으로 좌우 대칭이면서 가장 많은 스위치 포함하는 구간의 스위치 상태 바꿈







#마지막 상태 출력(1번 스위치~마지막 스위치/한 줄에 20개씩)
#켜진 스위치 :1 , 꺼진 스위치: 0, 사이에 빈칸 1