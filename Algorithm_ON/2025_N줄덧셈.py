# num = int(input())
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum) 


# n = int(input())
# ls = []
# for i in range(n+1):
#     if n % i == 0:
#     	ls.append(i)
# print(*ls)


A, B = map(int, input().split())
#가위 바위 보 123(1, 2)(1, 3)(2, 1)(2, 3)(3, 1)(3, 2)
if A == 1 and B == 2:
    print('B')
if A == 1 and B == 3:
    print('A')
if A == 2 and B == 1:
    print('A')
if A == 2 and B == 3:
    print('B')
if A == 3 and B == 1:
    print('B')
if A == 3 and B == 2:
    print('A')