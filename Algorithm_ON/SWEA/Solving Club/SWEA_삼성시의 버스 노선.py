import sys
sys.stdin = open('삼성시의버스노선.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #N개의 버스노선
    bus_nosun = [list(map(int, input().split())) for _ in range(N)] #각 버스노선에서 서는  정류장
    station_num = int(input()) #버스 정류장 개수
    cnt_lst = [0]*station_num
    station_num_arr = [int(input()) for a in range(station_num)] #버스 정류장 번호 리스트
    # for k in range(1, station_num+1):
    for i in range(N):
        for j in range(bus_nosun[i][0], bus_nosun[i][1]+1): #A1 : 1~3까지
            for l in range(station_num):
                if j == station_num_arr[l]:
                    cnt_lst[l] += 1
    print('#%d'%(tc), end = ' ')
    print(*cnt_lst)




