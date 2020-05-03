a=int(input())
for i in range(a):
    b=input().split()
    c=input().split()
    n=0
    while True:
        d=int(c[n])
        e=int(c[n+1])
        if d==e:
            n=n+1
        else:
            break
    while True:
        if d<e:
            e=e%d
        else:
            d=d%e
        if d*e==0:
            f=d+e
            break
    g=int(b[1])
    h=[]
    h.append(int(c[n])//f)
    for j in range(n,g-1):
        h.append(f)
        f=int(c[j+1])//f
    h.append(f)
    for j in range(0,n):
        h.insert(0,h[1])
    k=list(set(h))
    k.sort()
    l=""
    for j in range(g+1):
        m=k.index(h[j])
        l=l+chr(m+65)
    print("Case #{0}: {1}".format(i+1,l))