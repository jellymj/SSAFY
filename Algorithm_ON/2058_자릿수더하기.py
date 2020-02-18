n = int(input())
length = len(str(n))    
s = str(n)
sum = 0
for i in range(length):
    sum += int(s[i])
print(sum)