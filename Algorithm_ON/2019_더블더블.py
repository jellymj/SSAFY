n = int(input())
lst = []

for i in range(n+1):
    lst.append(str(2**i))

print(' '.join(lst))