a=int(input())
for i in range(a):
    b=int(input())
    c=list(range(b))
    f=[]
    g=[0]*b
    for j in range(b):
        e=input().split()
        f.append(list(range(int(e[0]),int(e[1]))))
    for j in range(1,1440):
        h=0
        for k in range(b):
            if j in f[k]:
                h=h+1
        if h>2:
            g="IMPOSSIBLE"
            break
    if g=="IMPOSSIBLE":
        print("Case #{}: {}".format(i+1,g))
    else:
        m=[]
        while c!=[]:
            if m==[]:
                d=c.pop(0)
                g[d]="C"
            else:
                d=m.pop(0)
            for j in c:
                for k in f[d]:
                    if k in f[j]:
                        if g[d]=="C":
                            g[j]="J"
                        else:
                            g[j]="C"
                        m.append(j)
                        break
            for j in m:
                if j in c:
                    c.remove(j)
        print("Case #{}: ".format(i+1),end="")
        for j in range(b):
            print(g[j],end="")
        print("")