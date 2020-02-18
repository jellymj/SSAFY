'''
T = int(input())
tc = 0
if 1 <= T <= 50:
    for i in range(0, T):
        max = 0
        min = 1000000
        N = int(input())
        Num_list = list(map(int, input().split()))
        for j in range(0, N):
            if 1 <= Num_list[j] <= 1000000 and 5 <= N <= 1000:
                if max < Num_list[j]:
                    max = Num_list[j]
        for j in range(0, N):
            if 1 <= Num_list[j] <= 1000000 and 5 <= N <= 1000:
                if min > Num_list[j]:
                    min = Num_list[j]
        tc += 1
        print('#'+str(tc)+' '+str(max-min))

'''
T = int(input())
tc = 0
result = 0
for i in range(0, T):
    N = int(input())
    num2 = list(map(int, input().split()))
    max1 = 1
    min1 = 1000000
    
    for a in range(0, N):
        if max1 < num2[a]:
            max1 = num2[a]
    for b in range(0, N):
        if min1 > num2[b]:
            min1 = num2[b]
    tc += 1
    result = max1 - min1
    print('#%d %d' % (tc, result))
