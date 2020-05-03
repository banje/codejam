import math
def i(g,h,c):
    global p
    if c[-g]=="1":
        if h==1:
            while h<=g:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h+1
            h=h-1
        else:
            while h>0:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h-1
            h=h+1
    else:
        print(g,h)
        p=p+math.comb(g-1,h-1)
    g=g+1
    if h!=1:
        h=h+1
    return [g,h]
a=int(input())
for z in range(a):
    b=int(input())
    print("Case #{}:".format(z+1))
    c=bin(b)[2:]
    d=c.count("0")
    g=1
    h=1
    p=0
    if d==0:
        while g<=len(c):
            [g,h]=i(g,h,c)
    elif b>15:
        e=c.find("10")
        f=len(c)-e
        while g<f:
            [g,h]=i(g,h,c)
        if h==1:
            while h<=g-3:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h+1
            g=g-1
            h=h-1
            while h<=g:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h+1
            if d+1!=len(c):
                g=g+1
                print(g,h)
                p=p+math.comb(g-1,h-1)
                g=g+1
                h=h+1
                while g<=len(c):
                    [g,h]=i(g,h,c)
                j=f-2-d
                while j>0:
                    print(g,h)
                    p=p+math.comb(g-1,h-1)
                    g=g+1
                    if h!=1:
                        h=h+1
                    j=j-1
        else:
            while h>3:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h-1
            g=g-1
            while h>0:
                print(g,h)
                p=p+math.comb(g-1,h-1)
                h=h-1
            if d+1!=len(c):
                g=g+1
                h=h+1
                print(g,h)
                p=p+math.comb(g-1,h-1)
                g=g+1
                while g<=len(c):
                    [g,h]=i(g,h,c)
                j=f-2-d
                while j>0:
                    print(g,h)
                    p=p+math.comb(g-1,h-1)
                    g=g+1
                    if h!=1:
                        h=h+1
                    j=j-1
    else:
        while g<=b:
            print(g,1)
            p=p+math.comb(g-1,0)
            g=g+1
    print(p)