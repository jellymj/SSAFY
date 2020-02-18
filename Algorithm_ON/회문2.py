import sys
sys.stdin = open('input_회문2.txt', 'r')


T = 10

for tc in range(1, T+1):
    palin_arr = [list(input())for _ in range(100)]
    count = 0
    for length in range(100):
        check_n = length >> 1
    for idy in range(100):
        for idx in range(100):
            for check in range(check_n):
                if palin_arr[idy][idx+check] != palin_arr[idy][idx +length -1 -check]:
                    break
            else:
                count += 1
    for idx1 in range(100):
                   
