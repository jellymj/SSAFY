import sys
sys.stdin = open('input.txt', 'r')

minsum = 987654321

def GetSome(here, sofar):  #sofar는 경로를 되돌아올때 더하는 값도 되돌리기 위해 쓰는 변수. 흔적을 지우는 역할.
    global goal, minsum   #goal은 목표 지점 / minsum은 ???뭐냐
    # if sofar < minsum : return          없애는 대신 Line15 에다가 조건 하나 추가
    if here == goal:        #
        if sofar < minsum:
            minsum = sofar
            return

    for next in range(goal+1):
        if MyMap[here][next] and not Visited[next] and sofar+MyMap[here][next] < minsum :
            Visited[next] = True
            GetSome(next, sofar + MyMap[here][next])
            Visited[next] = False

T = int(input())
for tc in range(1, T+1):
    goal, E = map(int, input().split())

    MyMap = [[0] * (goal+1) for i in range(goal+1)]
    Visited = [0] * (goal + 1)
    parent = [0] * (goal + 1)
    for i in range(E):
        start, end, cost = map(int, input().split())
        MyMap[start][end] = cost
        MyMap[end][start] = cost
    Visited[1] = True
    GetSome(1, 0)
    if minsum != 987654321:
        print('#%d' % tc, minsum)
    else:
        print('#%d - 1' % tc)

    #최소 경로 찍는거.
    # here = 7
    # while here!=1:
    #     print(Parent....)