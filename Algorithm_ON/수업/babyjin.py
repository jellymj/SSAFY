'''
num = 101253 #Baby Gin 확인할 6자리수 문자열
c = [0]*12 # 6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i<10:
    if c[i] >=3 : #triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri +=1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >=1 :
        c[i]-=1
        c[i+1]-=1
        c[i+2]-=1
        run += 1
        continue
    i += 1
if run + tri == 2 : print("Baby Gin")
else : print("Not Baby Gin")
    '''
   
def Counting_Sort(inp, out, k)
#inp [1 ... n] --- 입력 배열(1 to k)
#out [1 ... n] --- 정렬된 배열
#cnt [1 ... k] --- 카운트 배열

cnt = [0] * k

for i in range(1, len(out)) :
    cnt[inp[i]] += cnt[inp[i-1]]

for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]   

#idx = 0
for i in range(len(out)-1, -1, -1):
    out[cnt[inp[i]]-1] = inp[i]
    cnt[inp[i]] -= 1

def Counting_Sort()