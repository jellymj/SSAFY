T = 10  #테스트 케이스 10


for tc in range(1, T+1):
    N = int(input()) #각 테스트 케이스 가로 길이 (only건물들 개수가 아님_ 0인 케이스도 포함)
    # 빌딩수는 N-4
    building_heigt = list(map(int, input().split())) #각 건물들 최대층(건물 없을시에는 값이 0)

    count = 0
    for i in range(2, N-2):#첫 빌딩~마지막 빌딩
        if building_heigt[i] == max(building_heigt[i-2:i+3]):
            count += building_heigt[i] - max(building_heigt[i-2], building_heigt[i-1], building_heigt[i+1], building_heigt[i+2])
    print('#%d %d' %(tc, count))   
       
       
       
        #list index 0, 1, -1, -2인 경우는 따로 계산해야할까??



    # count = 0    
    # building_height = list(map(int, input().split()))
    # for i in range(2, len(building_height)-2):#3번째~뒤에서 3번째까지만
    #     if (building_height_lst[i] > building_height_lst[i-1]) and (building_height_lst[i] > building_height_lst[i-2]) and (building_height_lst[i] > building_height_lst[i+1]) and (building_height_lst[i] > building_height_lst[i+2]):
    #         count += 1
    # if (building_height_lst[0]> building_height_lst[1]) and (building_height_lst[0]> building_height_lst[2]):
    #     count += 1
    # if (building_height_lst[1]> building_height_lst[0]) and (building_height_lst[0]> building_height_lst[2]) and (building_height_lst[0]> building_height_lst[3]):
    #     count += 1
    # if (building_height_lst[-1]> building_height_lst[-2]) and (building_height_lst[-1]> building_height_lst[-3]):
    #     count += 1
    # if (building_height_lst[-2]> building_height_lst[-1]) and (building_height_lst[-2]> building_height_lst[-3]) and (building_height_lst[0]> building_height_lst[-4]):
    #     count += 1
    # print(count)       