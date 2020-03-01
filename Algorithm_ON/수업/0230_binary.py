a = [2, 4, 7, 9, 11, 19, 23]
#7을 찾는 경우!
'''
def binarySearch(a, key):
    key = 7
    for i in range(0, len(a)-1):
        if key < a[(len(a)//2 + 1)]:
'''





arr1 = [2, 4, 7, 9, 11, 19, 23]  #리스트 안의 숫자는 int형?
key = int(input())
#      0  1  2  3   4   5   6
# 중간값이 끝값보다 작거나 같으면
def binarySearch(arr):
    start = 0
    end = len(arr)-1 #arr의 마지막 값

    while (start <= end): #처음 값
        mid = (start+end)//2  #4
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False


print(binarySearch(arr1, key))