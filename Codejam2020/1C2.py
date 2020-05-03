a=int(input())
for z in range(a):
    b=int(input())
    d=[]
    for y in range(26):
        d.append(0)
    for y in range(10000):
        c=input().split()
        e=c[1]
        for x in range(len(e)):
            f=ord(e[x])-65
            d[f]=d[f]+1
    g=[]
    for y in range(26):
        if d[y]!=0:
            g.append([d[y],chr(y+65)])
    g.sort()
    h=g[1:]
    h.sort(reverse=True)
    print("Case #{}: {}".format(z+1,g[0][1]),end="")
    for y in range(9):
        print(h[y][1],end="")
    print("")