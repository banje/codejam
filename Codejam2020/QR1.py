a=int(input())
for i in range(a):
    b=int(input())
    c=[]
    for j in range(b):
        c.append(list(map(int,input().split())))
    d=0
    e=0
    f=0
    for j in range(b):
        d=d+c[j][j]
        if len(set(c[j]))!=b:
            e=e+1
    for j in range(b):
        g=[]
        for k in range(b):
            g.append(c[k][j])
        if len(set(g))!=b:
            f=f+1
    print("Case #{}: {} {} {}".format(i+1,d,e,f))