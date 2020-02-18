# DFS 연습문제 3

MyMap = [[0]*8 for i in range(8)]
Data = list(map(int, input().split()))
visited = [0]*8
stack = []
road = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

for i in range(len(road)/2):
    start = [2*i] 
    end = [2*i +1]
    MyMap[start][end] = 1
    MyMap[end][start] = 1
# 만약 노드가 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7 이라면
# MyMap에 해당 값 1로 채워넣어줌
#     1  2  3  4  5  6  7
# 1      1  1
# 2   1        1  1
# 3   1                 1
# 4      1           1
# 5      1           1
# 6            1  1     1
# 7         1        1

#def here: visited에 here 값을 append
#def next : 노드 7까지

def findnext(here): #다음 노드로 갈 곳을 찾는 함수
    for next in range(8):
        if MyMap[here][next] and not visited[next]:  #???
            return next

def DFS(here):
    stack.append(here)
    print(here)
    visited[here] = 1

    while stack: #stack에 뭐가 들어있으면
        next = findnext(here)
        while next:
            here = next
            print(here)
            visited[here] = 1
            stack.append(here)
            next = findnext(here)
        here = stack.pop() 

print(DFS(1))


#재귀

#연습 문제 3 DFS
data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
node = len(list(set(data)))+1   #0부터 7까지로 체크 하기
line = len(data)//2
map_list = [[0 for _ in range(node)] for _ in range(node)]
visited = [0] * node #visitlist 한번 방문했던 곳을 다시 가지 않기 위해서 집어 넣어 줄거임

for i in range(line):
    map_list[data[2*i]][data[2*i+1]]=1
    map_list[data[2 *i+1]][data[2 * i]] = 1

def DFS(here):
    print(here) #here = 1  -> 1 출력
    visited[here] = True  #사다리 라면 data[here]=99 이런식으로 길을 바꿔줌 !! 길을 지워주면 다시 돌아가지 않는다.
    for next in range(1,node):
        if map_list[here][next]==1 and not visited[next]:  #연결 되어있는 곳 : map 상에서 1이 있는 거 for문 돌려 보기.. visit 있으면 패스
            DFS(next)# 연결돼있는 곳에 가기

DFS(3)