T = int(input())

def find(node_start_num):
    
    for i in range(E):
        if nod_info[i][0] == node_start_num:
            node_start_num = nod_info[i][1]
    return nod_info[i][1]
    
for tc in range(1, T+1):
    arr = []
    result = arr[-1]
    V, E = map(int, input().split())
    nod_info = [list(map(int, input().split())) for _ in range(E)]
    # print(nod_info)
    start, end = map(int, input().split()) 

    while result == end:
        arr.append(find(start))
    print(result)
#######################################

def Search(start,goal):
    global result  #단일 변수는 global 선언해줘야함(리스트는 걍 써도됨)
    visited[start] = 1

    if start == goal:
        result = 1
        return  #return result안해도 됨??

    for end in range(1,node+1):
        if my_map[start][end] == 1 and not visited[end]:  #visited의 존재 이유는 무엇? 어차피 my_map에 1 떠있으면 갔다는 의미아닌가?
            Search(end,goal)
    # else:
    #     result = 0


T = int(input())
for case in range(1,T+1):
    node, edge = map(int,input().split())
    edge_list = [list(map(int,input().split())) for _ in range(edge)]
    start, goal = map(int,input().split())
    visited = [0] * (node + 1)   #방문한 곳 리스트
    my_map = [list(0 for _ in range(node+1)) for _ in range(node+1)] # 간선 경로 표시하는 매트릭스
    for e in edge_list:
        my_map[e[0]][e[1]] += 1  #걍 =1하면 안됨?
    result = 0
    Search(start,goal)


    print('#{}'.format(case),end=' ')

    if result == 1:
        print('1')
    else:
        print('0')

