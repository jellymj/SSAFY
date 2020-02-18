T = int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())
    m = M // N
    n = M % N

    print('#%d %d %d' % (tc, m, n))