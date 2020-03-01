import sys
sys.stdin = open('스타트와링크.txt', 'r')

def track(depth, ans):
    if depth == N/2:
        result_start = list(ans)
        result_link = []
        sum_start = 0
        sum_link = 0
        sum_start_arr = []
        # sum_link_arr = []

        for number in numbers:
            if number not in result_start:
                result_link.append(number)

            # for i in range(N//2 - 1):
            #     if result_start[i] > result_start[i + 1]:
            #         return
        # print(result_link, end=' ')
        # print(result_start)
        for j in range(N//2):  #link안의 숫자만큼 돌면서
            for k in range(N//2):
                sum_link += S[result_link[j]-1][result_link[k]-1]
                sum_start += S[result_start[j] - 1][result_start[k] - 1]
        score_diff.append(abs(sum_start - sum_link))

    for number in range(ans[-1]+1, N+1):
        ans.append(number)
        track(depth+1, ans)
        ans.pop()

        # # if number in ans:
        # #     continue
        # # else:
        #     ans.append(number)
        #     track(depth + 1, ans)
        #     ans.pop()

N = int(input())  # 총 명수
S = [list(map(int, input().split())) for _ in range(N)]
numbers = list(range(1, N + 1))
score_diff = []
track(1, [1])
print(min(score_diff))
#
# for a in range(N):
#     track(0, [])
#     print(result_start)