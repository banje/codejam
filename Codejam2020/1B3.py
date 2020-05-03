a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    c=b[0]*(b[1]-1)
    d=b[0]-1
    e=[]
    f=0
    for k in range(b[0]-1):
        for j in range(b[1]-1):
            e.append(str(c)+" "+str(d))
            f=f+1
            c=c-1
        d=d-1
    print("Case #{}: {}".format(i+1,f))
    for j in e:
        print(j)