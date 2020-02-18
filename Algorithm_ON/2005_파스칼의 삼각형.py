# N줄로 출력
#def pascal 만들어보기!!


T = int(input())
# T = int(input())       # TC



for tc in range(1, T+1):
    N = int(input())  # N
    arr = [[0]*N for i in range(N)] #0으로 채워진 4*4 배열
    for j in range(N):  #0, 1, 2, 3
        arr[j][0] = 1
        arr[j][j] = 1
    for k in range(2, N):  #2, 3
        for z in range(1, N-1): #1, 2
            arr[k][z] = arr[k-1][z-1] + arr[k-1][z]
    print('#%d' %(T))

    for m in range(N):
        result = ''
        for p in range(N):
            if arr[m][p] != 0:
                result += str(arr[m][p]) + ' '
        print(result)
# 1
# 1 1
# 1 2 1

    # print(arr[m], end = '\n')
# print(arr, end = '\n')
# for m in range(N):
#     arr[m].remove(0)
#     print(arr)
# for i in range(N):
#     if arr[][]
#     print(arr[i])
# print(arr)
# for i in range(N): #0, 1, 2, 3
#     print(arr[i][i])
    # for n in range(N):#0, 1, 2, 3
    #     if arr[i][n] != 0:
    #
    #         print(arr[i][n])



# for i in range(N):   # 0, 1, 2
#     j = i+1
#     for b in range(1, N+1):  #1, 2, 3
#         print(arr[i][i])
#         arr[i]
#     print(arr[i])

# i가 1씩 증가할 때마다 리스트 요소 수도 1개씩 늘어남
# 맨 뒷 요소는 1로 채워줌.
#현재 리스트의 리스트(i-1)값 + 위쪽 리스트(i)값  == 현재 리스트(i)값




'''
#2005 파스칼 삼각형
from pprint import pprint
 
def tri_pascal(n):
    ans=''
    pascal =[[0 for i in range(n)] for i in range(n)]
    #일단 처음 수와 끝수에 1 넣기
    for i in range(n):
        pascal[i][0]=1
        pascal[i][i]=1
        for j in range(1,i):
            pascal[i][j]=pascal[i-1][j]+pascal[i-1][j-1]
 
    for i in range(n):
        ans+=' '.join(list(map(str, pascal[i][:i+1])))+'\n'
    return ans
 
T=int(input())
for z in range(T):
    n = int(input())
    print("#{}".format(z+1))
    print(tri_pascal(n),end="")

'''


#print('#%d ' % (tc))

'''
def comb(n,r):
    n1 = 1
    r1 = 1
    r2 = 1
    for i in range(1,n+1):
        n1 *= i
    for j in range(1,r+1):
        r1 *= j
    for k in range(1 , n - r +1):
        r2 *= k
 
    return n1/(r1*r2)
 
T = int(input())
 
for case in range(1, T +1):
    print(f'#{case}')
    n_last = int(input())
    print(1)
    for n in range(1,n_last):
        pa_lis = []
        # print(n)
        for r in range(0,n+1):
            pa_lis.append(str(int(comb(n,r))))
        result = pa_lis
        print(' '.join(result))

'''