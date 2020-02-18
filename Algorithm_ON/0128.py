import sys
sys.stdin = open("1206input.txt", "r")

tc = 10

for i in range(1, tc + 1):
    #입력 N. list
    width = int(input())
    building = list(map(int, input().split()))
    #map : input받은거를 int로 하나하나 적용해줌
    sum = 0
    for j in range(2, width-2):
        max1 = max(building[j-2], building[j-1])
        max2 = max(building[j+1], building[j+2])
        if max1 >= max2:
            max3 = max1
        else:
            max3 = max2
        if building[j] > max3:
            sum += building[j] - max3
    print("#{0} {1}".format(i, sum))
        #cnt = Hs[j] 에서 조망권 확보된 수 계산
        #vSum += cnt


    #출력 조망권확보세대수의 합
"""
for i in range(1, 11):
    width = int(input())
    buildings = list(map(int, input().split()))
    sum = 0
    for j in range(2, width-2):
        max1 = max(buildings[j-2], buildings[j-1])
        max2 = max(buildings[j+1], buildings[j+2])
        maximum = max1 if max1 >= max2 else max2
        if buildings[j] > maximum:
            sum += buildings[j] - maximum
    print('#{0} {1}'.format(i, sum)
          """


def getMax(idx):
    tmax = heights[idx-2]
    return tmax
TC = 10

for to in range(1, Tc+1):
    N = int(input())
    Hs = list(map(int.input().split()))

    vcnt = 0
    for i in range(2, N-2):
        tm = max