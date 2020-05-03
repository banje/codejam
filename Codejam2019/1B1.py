a=int(input())
for i in range(a):
    b=input().split()
    c=int(b[1])
    b=int(b[0])
    g = [0] * (c + 1)
    h = [0] * (c + 1)
    for j in range(b):
        d=input().split()
        e=int(d[1])
        f=d[2]
        d=int(d[0])
        if f=="E":
            for k in range(d+1,c+1):
                g[k]=g[k]+1
        if f=="W":
            for k in range(d-1,-1,-1):
                g[k]=g[k]+1
        if f=="N":
            for k in range(e+1,c+1):
                h[k]=h[k]+1
        if f=="S":
            for k in range(e-1,-1,-1):
                h[k]=h[k]+1
    l=g.index(max(g))
    m=h.index(max(h))
    print("Case #{}: {} {}".format(i+1,l,m))