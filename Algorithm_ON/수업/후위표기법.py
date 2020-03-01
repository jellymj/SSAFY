# m = list(input())
# priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
# stack = []
# result = []
# for i in range(len(m)):
#     if list[i] in priority:
#         stack.append()
#     else:
#         result.append()


##############################################################

a = input()
sta = []
dic = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
for i in a:
    if i in dic.keys():
        if i == ')':
            while sta[-1]!='(':      # ((2+3)*4) 같은 경우???
                print(sta.pop(), end = '')
            sta.pop()
        elif i == '(':
            sta.append(i)
        else:
            while len(sta)>0 and dic[sta[-1]]>=dic[i]: #스택에 뭐가 들어있고, 스택의 마지막 부호의 키값이 현재 들어가는 부호의 키값보다 크거나 같을때까지
                print(sta.pop(), end = '')             # 스택의 마지막 것을 팝해서 프린트한다.
            sta.append(i)                              # while문이 false이면 그냥 스택에 현재 요소를 넣는다.
    else:   #숫자는 다 그냥 프린트 해줌.
        print(i, end = '')
for i in range(len(sta)):
    print(sta.pop(), end = '')


#################################################

N=list(input())
result=[]
stack =[]
top=-1
for i in range(len(N)+1):
    if i==len(N):
        while top>-1:
            a=stack.pop()
            top-=1
            result.append(a)
    elif N[i]=='(':
        stack.append(N[i])
        top+=1
    elif N[i]==')':
        while stack[-1]!='(':
            a=stack.pop()
            top-=1
            result.append(a)
        top-=1
        stack.pop()
    elif N[i] in '0123456789':
        result.append(N[i])
    elif N[i]in'+-':
        while stack[-1] in'+-*/':
            a=stack.pop()
            top-=1
            result.append(a)
        top+=1
        stack.append(N[i])
    elif N[i]in'*/':
        while stack[-1] in '*/':
            a=stack.pop()
            top-=1
            result.append(a)
        stack.append(N[i])
        top+=1
print(*result)