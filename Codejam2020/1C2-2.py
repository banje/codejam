a=int(input())
for z in range(a):
    b=int(input())
    d=[]
    for y in range(26):
        d.append(0)
    i=0
    j=set()
    for y in range(10000):
        c=input().split()
        if i==0:
            for x in range(len(c[1])):
                j.add(c[1][x])
            if len(j)==10:
                i=1
        e=c[1][0]
        f=ord(e)-65
        d[f]=d[f]+1
    g=[]
    for y in range(26):
        if d[y]!=0:
            g.append([d[y],chr(y+65)])
    for y in g:
        if y[1] in j:
            j.remove(y[1])
    g.sort(reverse=True)
    h=list(j)
    print("Case #{}: {}".format(z+1,h[0]),end="")
    for y in range(9):
        print(g[y][1],end="")
    print("")