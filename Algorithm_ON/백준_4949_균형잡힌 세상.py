import sys
sys.stdin = open('4949.txt', 'r')

dict = [0]*128
dict[ord(']')] = '['
dict[ord(')')] = '('
stack = []

while 1:
    str_list = list(input())
    check_count = 0
    for i in range(len(str_list)):
        if str_list[i] == '.': #종료조건
            break
        if str_list[i] == "(" or str_list[i] == "[": #
            stack.append(str_list[i])
        elif str_list[i] == ')' or str_list[i] == ']':
            if len(stack) == 0:
                check_count += 1
                break

            else:
                if str_list[i] == ")" or str_list[i] == "]":
                    if stack[-1] == dict[ord(str_list[i])]:
                        stack.pop()
    if len(stack) != 0 or check_count != 0:
        print("no")
    else:
        print("yes")
        stack = []
        count = 0