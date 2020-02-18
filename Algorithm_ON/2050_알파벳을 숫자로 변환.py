alpha = list(str(input()))
length = len(alpha)
lst = []
for i in range(1, length+1):
    lst.append(i)
print(*lst, sep = ' ')

