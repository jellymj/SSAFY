
arr = [64, 25, 10, 22, 11]


#def SelectionSort(a[], len(arr): #선택 정렬 함수(배열 a[], 요소 수 n개)
for now in range(len(arr)):  # 0~5
    min_1 = arr[now]         # 인덱스0~5까지 현재 값을 초기 최소 값으로 설정
    for i in range(now,len(arr)): #현재값~리스트 마지막 값까지 for문
            #min_1=64
            if min_1 > arr[i] : #만약 현재값보다 작은 값이 있다면
                min_1 = arr[i] #min값에 현재값을 대입
                wheremin = i   #현재 인덱스값을 알려주는 wheremin 변수를 생성
    arr[now], arr[wheremin] = arr[wheremin], arr[now] #작은 값을 현재 위치로 이동
print(arr)
#print(arr)










