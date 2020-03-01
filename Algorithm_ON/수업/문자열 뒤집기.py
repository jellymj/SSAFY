Data = list(input())

start = 0
end = len(Data) -1

while start < end:
    Data[start], Data[end] = Data[end], Data[start]
    start += 1
    end -= 1
print(Data)
