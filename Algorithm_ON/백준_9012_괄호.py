T = int(input())

for tc in range(1, T+1):
    stack = []
    result = "YES"
    s = list(input())
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        if s[i] == ')':
            stack.pop
            if len(stack) == i-len(stack)+1

            if len(stack) == 0:
                result = "NO"
                break
            else:
                stack.pop
            #     if len(stack) != 0:
            #         result =
        if len(stack) != 0:

            result = "NO"
        else:
            result = "Yes"
            
    print(result)



      