T = int(input())

P, Pa, Pb = map(int, input().split()) #전체 페이지/a가 찾는 쪽 / b가 찾는 쪽

for tc in range(T):
    c = P / 2
    count_a = 0
    while (Pa == c): #a

        l = 0
        r = P

        mid = (l + r)/2
        if (Pa > mid):
            l = mid
            count_a += 1
        elif (Pa < mid):
            r = mid
            count_a += 1
        else: #찾았을 때
            count_a += 1

    print(count_a)

'''
    while (Pb ==c): #b
        lb = 0
        rb = Pb
        count_b = 0
        mid = (lb + rb) / 2
        if (Pb > mid):
            mid = l
            count_b += 1
        elif (Pb < mid):
            mid = rb
            count_b += 1
        else:  # 찾았을 때
            count_b += 1
    return count_b

    if (count_a > count_b): #탐색 번수 count해서 낮은 쪽이 이긴것. 낮은 쪽 출력

        print('#%d A' % (tc+1))
    elif (count_a < count_b):
        print('#%d B'% (tc+1))
    else:
        print('#%d 0' % (tc+1))
    #탐색 번수 count해서 낮은 쪽이 이긴것. 낮은 쪽 출력
    '''