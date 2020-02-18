T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, (input().split()))
    time_lst = list(map(int, input().split()))  # 손님이 각각 몇초에 오는지?
    num_bbang = 0  # 붕어빵 재고
    result = "Possible"

    for i in range(11112):  # 시간의 흐름

        if (i % M) == 0 and (i != 0):  # M초 지날 때마다 //  i가 0일때는 포함하면 안됨!
            num_bbang += K  # 붕어빵개수는 K개씩 늘어남

        for j in time_lst:  # 각 손님들이 오는 시간을 돌려봄
            # if j < i:
            #     result =

            if j == i:
                # num_bbang -= 1
                if num_bbang == 0:
                    result = "Impossible"
                    break
                num_bbang -= 1
                #
                # if num_bbang < 0:
                #     result = a
                # else:
                #     result = b

    print('#%d %s' % (tc, result))
