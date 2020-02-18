#'1''2''3'을 123으로 바꾸기(문자열을 숫자로)
digit = 0
value = 0
data = ['1', '2', '3']
for i in range(3):
    digit += str(data[i])-'0'
    value += digit*(10**i)
print(value)
print(type(value))


#
# # (16진수로)
# Data = list(input())
# val = 0
# for now in range(len(Data)):
#     val*16
#     if '0' <= Data[now] <= '9':
#         val += ord(Data[now])-ord('0')
#     elif'A' <= Data[now] <= 'F':
#         val += (ord(Data[now])-ord('A') + 10
# print(val)
#
#
# #123을 '1''2''3'으로 바꾸기(숫자를 문자열로)
#
# Data = int(input())
# Beint=''
# while True:
#     r = Data % 10
#     Beint = Beint + chr(r + ord('0'))
#     Data //= 10
#     if Data == 0:break
# ans =''
# for i in range(len(Beint) -1, -1, -1):
#     ans = ans + Beint[i]