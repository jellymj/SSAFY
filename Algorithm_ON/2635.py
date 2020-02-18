num_1st = int(input()) #첫번째 수로 양의 정수가 주어진다
count = 0
for num_2nd in range(0, 101):
    if num_1st - num_2nd < 0:
        break
    elif 2*num_2nd - num_1st < 0: #num_2nd - num_3rd < 0, num_3rd = num_1st - num_2nd
        break

N = int(input())
max_1 = 0
max_list = []
for i in range(N+1):
    result = [N, i]
    j = 0
    while(True):
        a = result[j] - result[j+1]
        if a <= -1:
            break
        result.append(a)
        if max_1 < len(result):
            max_1 = len(result)
            max_list = result[:] #result의 모든 아이템
        j += 1
print(max_1)
for e in max_list:
    print(e, end = " ")
print()

    