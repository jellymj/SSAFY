import sys
sys.stdin = open('1268.txt', 'r')

N = int(input()) #학생수
mat = [list(map(int, input().split())) for _ in range(N)] #학생 몇반이었는지
check_lst = [[0]*5 for _ in range(N)] #같은 반이었던 적 몇번인지 셀 리스트
cnt = [0]*N
result = 0

for i in range(N):
    visited = ['F'] * N
    for j in range(5):
        for k in range(N):
            if i == k:
                continue
            if mat[i][j] == mat[k][j] and visited[k] != 'T':
                check_lst[i][j] += 1
                visited[k] = 'T'
# print(check_lst)
for l in range(N):
    for m in range(5):
        cnt[l] += check_lst[l][m]
result = max(cnt)
# print(cnt)
# print(cnt.count(result))
#
print(cnt.index(result) + 1)



