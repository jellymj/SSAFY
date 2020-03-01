import sys
sys.stdin = open('2652.txt', 'r')

N = int(input()) #판의 한 변의 길이
fuck_shape = list(map(int, input().split())) #ㅗ자 모양
d_mat = [list(map(int, input().split())) for _ in range(N)]

#일단 ㄷ자 블록 모양 비교

# 판 벗어나면 x

#다른 ㄷ 블록이랑 겹치면 X

#만족하는 ㅗ 없으면 0출력
