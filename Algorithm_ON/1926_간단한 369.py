N = int(input())
result = ['']*100
arr = []
for i

for idx, val in enumerate(arr):
    if '3' in val or '6' in val or '9' in val:
        result[idx] += '-' * (val.count('3') + val.count('6') + val.count('9'))
    else:
        result[idx] = idx+ 1

for i in range(len(result)):
    print(*result)
    

# n = int(input())
# result = [''] * 100   #왜 있는거?? => 실제 원하는 값 넣어놓을 리스트
 
# temp = []   # idx, val값 얻기 위한 리스트
# for i in range(1, n+1):
#     temp.append(str(i))
 
# for idx, val in enumerate(temp):  #enumerate 함수 : index, value 값 반환
#     if '3' in val or '6' in val or '9' in val:
#         result[idx] += '-' * (val.count('3') + val.count('6') + val.count('9'))
#     else:
#         result[idx] = idx+1
 
# for i in range(len(result)):
#     print(result[i], end = ' ')
 
       	  



