import sys

'''
def MyAbs(y,x):
    if y > x: return y - x
    else: return x - y

def isSafe(y, x):
    if y >= 0 and y < 5 and x >= 0 and x < 5: return True
    else: return False


#5*5초기화
Data = [[0  for _ in range(5)] for _ in range(5)]

#5*5에다가 숫자 집어넣는거
for i in range(5):
    Data[i]=list(map(int, input().split()))


dy = [-1, 1, 0,0 ]
dx = [0, 0, -1, 1] #상하좌우

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y +dy[dir]
            newX = x + dx[dir]
            if isSafe(newY,newX):
                sum += MyAbs(Data[y][x], Data[newY][newX])
print(sum)
'''
#연습문제 2 - 합이 10
n = int(input()) #len(arr)
arr = list(map(int, input().split()))
#subset = []


for i in range(1<<n): #부분 집합의 개수  ->  2^10
    subset = []
    # print()
    for j in range(n):  #원소의 수만큼 비트 비교(0~10)
        if (i & (1<<j)):

            #i의 j번째 비트가 1이면 ?///// 2^6과 2^7 자리가 둘다 1인지. 자리 비교.
            subset.append(arr[j])
            # print(subset)
    # 조건을 만족하는 subset 생성되었음.
    if sum(subset)  == 10: #만족하는 subset 중에서 합이 10인 것을 찾음
        print(subset)


'''
#부분집합 구하기
n = 10
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)  #n:원소의 개수
for i in range(1<<n):  #부분 집합의 개수  ->  2^6
    for j in range(n): #원소의 수만큼 비트 비교(0~6)
        if i & (1<<j): #i의 j번째 비트가 1인지 아닌지 ///// 2^6과 2^7 자리가 둘다 1인지. 자리 비교.
            print(arr[j], end = ", ")
    print()
print()

'''

'''
for i in range(1<<n):
    for b in range(n+1):
        if i & (1<<b):
            arr = arr[b]
            for j in range (len(arr)):
                sumsum = sum(j)
                if sumsum == 0:
                    print(arr[j])

'''

'''
Data = list(map(int, input().split()))
num = 11
IsFound = False
for now in range(len(Data)):
    if num ==Data[now]:
        IsFound = True
            print("Found at %d" %now)
            break
if(IsFound ==False): 
    print("못찾았다")
'''


