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
        c=(2**(d)-1-b[0]-b[1])//2
        if c>0:
            e=bin(c)[2:]
        elif c<0:
            e=bin(c)[3:]
        else:
            e="0"
        e=e.zfill(d)
        f=[]
        for j in range(d):
            if e[-j-1]=="0":
                f.append(2**j)
            else:
                f.append(-(2**j))
        for j in range(2**d):
            g=bin(j)[2:].zfill(d)
            h0=0
            h1=0
            for k in range(d):
                if g[k]=="1":
                    h0=h0+f[k]
                else:
                    h1=h1+f[k]
            if h0==b[0]:
                if h1==b[1]:
                    h=""
                    for k in range(d):
                        if g[k]=="0":
                            if e[-k-1]=="0":
                                h=h+"N"
                            else:
                                h=h+"S"
                        else:
                            if e[-k-1]=="0":
                                h=h+"E"
                            else:
                                h=h+"W"
                    print("Case #{}: {}".format(i+1,h))
                    break