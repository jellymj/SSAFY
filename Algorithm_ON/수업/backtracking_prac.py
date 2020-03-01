# nQueen 문제

visitedX = [0] * 10
visitedIncrease = [0] * 10
visitedDecrease = [0] * 10
def GetSome(y):
    global ans
    if y > 4:
        ans += 1
        return
    for x in range(1, 5):
        if not visitedX[x] and not visitedIncrease[y + x] and not visitedDecrease[y-x+4]:
            visitedX[x] = visitedIncrease[y + x] = visitedDecrease[y - x + 4] = 1
            GetSome(y + 1)
            visitedX[x] = visitedIncrease[y + x] = visitedDecrease[y - x + 4] = 0
ans = 0
GetSome(1)