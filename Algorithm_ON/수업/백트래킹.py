
#부분집합 구하기
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [1, 0]

    if k == input:
        for i in range(1, input+1):
            if a[i] == True:
                print(i, end = "")
            print()
             #답이면 원하는 작업을 한다
    else:
        k+=1
        for i in range(2):
            a[k] = c[i]
            backtrack(a, k, input)
MAXCANDIDATES = 100
NMAX = 100  
a = [0] * NMAX
backtrack(a, 0, 3)

###############################################
#가지치기
def backtrack(a, k, input, s):
    if k ==(input-1):
        if s == 10:
            for i in range(input):
                if a[i] == 1:
                    print(P[i], end = " ")
                print()
    else:
        if s < 10:
            backtrack(a, k+1, input, s)
            a[k] = 1
            backtrack(a, k+1, input, s+P[k])
a = [0]*100
P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10, 0)

######################################################
#끝까지 다 가는거
def backtrack(a, k, input):
    #print("k = ", k, a)
    if k == input:
        psum = 0
        for i in range(input):
            if a[i] == 1:
                psum += P[i]
        if psum == 10:
            for i in range(input):
                if a[i] == 1:
                    print(P[i], end = " ")
            print()
        return
    else:
        a[k] = 0
        backtrack(a, k+1, input)
        a[k] = 1
        backtrack(a, k+1, input)
a = [0]*5
P = [1, 3, 6, 7, 10]
backtrack(a, 0, 5)

############################################
#수열 구하기
def perm_r_1(a, k, N):
    if k == N:
        print(a)
    else:
        in_perm = [False] * N
        c = [0]*N

        for i in range(k):
            in_perm[a[i]] = True
        ncandidates = 0
        for i in range(N):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        for i in range(ncandidates):
            a[k] = c[i]
            perm_r_1(a, k+1, N)

