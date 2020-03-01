import sys
sys.stdin = open("200128_2.txt", "r")

T = int(input())
tc = 0
result = 0
for i in range(0, T):
    num2 = list(map(int, input().split()))
    max1 = 1
    min1 = 1000000

    for a in range(0, len(num2)):
        if max1 < num2[a]:
            max1 = num2[a]
    for b in range(0, len(num2)):
        if min1 > num2[b]:
            min1 = num2[b]
    tc += 1
    result = max1 - min1
    print('# %d %d' % (tc, result))


'''
3
477162 658880 751280 927930 297191
565469 851600 460874 148692 111090
784386 279993 982220 996285 614710 992232 195265 359810 919192


T = 3
N = 5
Num_list = [477162, 658880, 751280, 927930, 297191]


import sys
sys.stdin = open("1207.txt", "r")

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
