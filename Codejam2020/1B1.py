a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    if (b[0]+b[1])%2==0:
        print("Case #{}: IMPOSSIBLE".format(i+1))
    else:
        d=1
        while True:
            if 2**(d-1)>(abs(b[0])+abs(b[1])):
                d=d-1
                break
            d=d+1
        e=[]
        for j in range(d):
            e.append(2**(j))
        if b[0]%2==0:
            c=len(bin(abs(b[0])))-3
            if b[0]!=0:
                e.remove(abs(b[0]))
            else:
                d=d+1
            for j in range(2**(d-1)):
                f=bin(j)[2:].zfill(d-1)
                g=0
                for k in range(d-1):
                    if f[k]=="1":
                        g=g+e[k]
                    else:
                        g=g-e[k]
                if g==b[1]:
                    h=""
                    for k in range(d-1):
                        if f[k]=="1":
                            h=h+"N"
                        else:
                            h=h+"S"
                    if b[0]>0:
                        h=h[:c]+"E"+h[c:]
                    elif b[0]<0:
                        h = h[:c] + "W" + h[c:]
                    print("Case #{}: {}".format(i+1,h))
                    break
            else:
                print("Case #{}: IMPOSSIBLE".format(i + 1))
        else:
            c=len(bin(abs(b[1])))-3
            if b[1]!=0:
                e.remove(abs(b[1]))
            else:
                d=d+1
            for j in range(2**(d-1)):
                f=bin(j)[2:].zfill(d-1)
                g=0
                for k in range(d-1):
                    if f[k]=="1":
                        g=g+e[k]
                    else:
                        g=g-e[k]
                if g==b[0]:
                    h=""
                    for k in range(d-1):
                        if f[k]=="1":
                            h=h+"E"
                        else:
                            h=h+"W"
                    if b[1]>0:
                        h=h[:c]+"N"+h[c:]
                    elif b[1]<0:
                        h = h[:c] + "S" + h[c:]
                    print("Case #{}: {}".format(i+1,h))
                    break
            else:
                print("Case #{}: IMPOSSIBLE".format(i + 1))