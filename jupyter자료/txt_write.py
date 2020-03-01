f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line{i}\r\n')
f.close()

with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line{i}\r\n')

with open('ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])