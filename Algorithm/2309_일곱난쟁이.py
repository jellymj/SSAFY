key_list = []
for i in range(9):
    key = int(input())
    key_list.append(key)

for i in range(1<<9):
    possible_lst = []
    for j in range(10):
        if i & (1<<j):
            possible_lst.append(key_list[j])
    if sum(possible_lst) == 100 and len(possible_lst) == 7:
        possible_lst = possible_lst

#오름차순 정렬

max_lst = []
for i in range(len(possible_lst)):
    max_lst.append(min(possible_lst))
    possible_lst.append(min(possible_lst))
    possible_lst.remove(min(possible_lst))
print(max_lst)
# for i in range(len(max_lst)):
#     result += ' ' + max_lst[i]
# print(result)