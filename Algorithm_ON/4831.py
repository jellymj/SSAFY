TC = int(input())
for tc in range(1, TC+1):
    K,N,M = map(int,input().split())
    station = list(map(int, input().split()))
    station_lst = [0] * (N+1)

    for i in range(len(station)):
        station_lst[station[i]] += 1

    start = 0
    end = K
    cnt = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if station_lst[i] == 1:
                start = i
            else:
                zero += 1

        if zero == K:
            cnt = 0
            break

        cnt += 1
        end = start + K

        if end >= N:
            break

    print('#%s %d'%(tc, cnt))

'''
T = int(input())
tc = 0
k, n, m = map(int, input().split())
bus = k #현재 위치?
cnt = 0 #충전횟수
check = 0 #마지막으로 충전한 위치
charge = m #충전소 위치한 정류장 위치
for t in range(1, T):
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