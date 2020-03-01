T = int(input())

for tc in range(1, T+1):
    sum = 0
    N = int(input())
    for num in range(N+1):
        if num%2 == 1:
            sum += num
        else:
            sum -= num
    print('#%d %d' %(tc, sum))