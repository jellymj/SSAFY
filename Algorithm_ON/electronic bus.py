
T = int(input())
tc = 0

#충전 위치 찾기.
#정류장 번호?

#충전소 가기 힘든 경우.
#종점에 도착할 수 없는 경우 => 0출력

for t in range(1, T):
    k, n, m = map(int, input().split())


#k = line[0] #이동할 수 있는 칸 수
#n = line[1] # 총 정류장 수(종점)
#m = line[2] #충전기가 설치된 정류장
    bus = k #현재 위치?
    cnt = 0 #충전횟수
    check = 0 #마지막으로 충전한 위치
    charge = m #충전소 위치한 정류장 위치


    while bus < n:                 #현재 위치가 총 종점에 도착하기 전까지 while문 돌려
        if bus != check:         #현재 위치가 마지막으로 충전한 위치가 아니라면,
            if bus in charge:      #만약 현재 위치가 충전소 위치한 정류장 전이라면
                check = bus        #마지막으로 충전한 위치에 현재 위치 대입
                cnt += 1           #한번 충전.
                for i in range(k):  # 이동할 수 있는 칸 수 안에서
                    bus += 1        #현재 위치에서 한칸 더 감.
            else:
                bus-= 1
                # 현재 위치 - 1
        else:                     #그게 아니라면(현재 위치가 마지막으로 충전한 위치라면)
            cnt = 0                 #충전 횟수에 0대입
            break
    tc += 1                          #테스트 케이스 번호

    print('#'+str(tc)+' ' +str(cnt))









'''
T = int(input())
tc = 0
if 1 <= T <= 50:
    for i in range(0, T):
        max = 0 #최대값을 찾아야 하니 디폴트값은 최소값으로
        min = 1000000 #최소값을 찾아야 하니 디폴트값은 최대값으로
        N = int(input()) # N개의 양의정수
        Num_list = list(map(int, input().split())) # 값 불러와서 하나하나 int로 된 리스트 만들기
        for j in range(0, N): #max찾기
            if 1 <= Num_list[j] <= 1000000 and 5 <= N <= 1000: # N의 조건과 ai의 조건
                if max < Num_list[j]:
                    max = Num_list[j]
        for j in range(0, N):#min찾기
            if 1 <= Num_list[j] <= 1000000 and 5 <= N <= 1000:# N의 조건과 ai의 조건
                if min > Num_list[j]:
                    min = Num_list[j]
        tc += 1
        print('#'+str(tc)+' '+str(max-min))
'''

