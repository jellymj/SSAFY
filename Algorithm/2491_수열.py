'''

len_N = int(input())  # 수열의 길이 len(N_arr)
N_arr = list(map(int, input().split()))  # N개의 숫자로 이뤄진 리스트
count1 = 1
count2 = 1
result1 = 0
result2 = 0
for i in range(len_N - 1):

    if N_arr[i + 1] >= N_arr[i]:
        count1 += 1

    # else:
    #    break
result1 = count1

for j in range(len_N - 1):

    if N_arr[j + 1] <= N_arr[j]:
        count2 += 1
    # else: #앞에 값이 커지고 있을 때 뒤에는 검사 안하고 break..

    #    break
result2 = count2
print(max(result1, result2))

'''



len_N = int(input())  # 수열의 길이 len(N_arr)
N_arr = list(map(int, input().split()))  # N개의 숫자로 이뤄진 리스트
count1 = 1
count2 = 1
count3 = 1
result1 = 0
result2 = 0
for i in range(len_N - 1):

    if N_arr[i + 1] >= N_arr[i]:
        count1 += 1

    else:  # 커지다가 작아지면
# 그 다음 i부터 다시 검사
# 다시 커지면 카운트 세주기(카운트하는 변수 하나 더 만들기)
# 카운트 변수끼리 크기 비교해주기(근데 그 카운트 변수가 몇개가 만들어질지는 모름)

        result1 = count1

for j in range(len_N - 1):

    if N_arr[j + 1] <= N_arr[j]:
        count2 += 1
    # else: #앞에 값이 커지고 있을 때 뒤에는 검사 안하고 break..

    #    break
        result2 = count2
print(max(result1, result2))

# 가장 긴 수열의 길이를 출력












