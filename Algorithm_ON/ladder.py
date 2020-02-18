import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T+1):
    arr_ladder = [lst(map(int, input().split()))]

print(arr_ladder)
#
# for x in range(100):
#     if Mymap[99][x] == 2: startX = x
#     x = startX
#     y = 99
#
#     whlie True:
#     #x-1 >0
#
#     #elif x+1 < 99
#
#
#     #else y-=1
#
#     #if y ==0: break