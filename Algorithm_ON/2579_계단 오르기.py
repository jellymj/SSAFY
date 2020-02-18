num_stair = int(input())


def Getsome(here):
    global ans, howmany
    if here > howmany:



        return
    if here == howmany:


        ans+=1
        return


     GetSome(here+1)
     GetSome(here+2)



howmany = 3
ans = 0
GetSome(0)
proint(ans)