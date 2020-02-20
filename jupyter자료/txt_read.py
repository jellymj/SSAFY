# f = open('ssafy.txt', 'r')
# all_text = f.read()
# print(all_text)
# f.close()

with open('ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)