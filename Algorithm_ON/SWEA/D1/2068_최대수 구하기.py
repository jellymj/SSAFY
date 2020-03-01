T = int(input())

for tc in range(1, T+1):
    max = 0
    lst = list(map(int, input().split()))
    for i in range(10):
        if lst[i]>max :
            max = lst[i]

    print('#%d %d' %(tc, max))