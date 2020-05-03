a=int(input())
for i in range(a):
    b=int(input())
    c=[]
    for j in range(b):
        d=input()
        d=d*(500//len(d)+1)
        c.append(d)
    e=""
    for j in range(500):
        f=0
        g=0
        h=0
        l=0
        for k in range(b):
            if c[k][j]=="R":
                f=1
                break
        for k in range(b):
            if c[k][j]=="S":
                g=1
                break
        for k in range(b):
            if c[k][j]=="P":
                h=1
                break
        if f*g*h==1:
            e="IMPOSSIBLE"
            break
        elif f+g==0:
            e=e+"S"
            break
        elif f+h==0:
            e=e+"R"
            break
        elif g+h==0:
            e=e+"P"
            break
        elif f*g==1:
            e=e+"R"
            for k in range(b):
                if c[k][j]=="S":
                    c[k]=0
                    l=l+1
        elif f*h==1:
            e=e+"P"
            for k in range(b):
                if c[k][j]=="R":
                    c[k]=0
                    l=l+1
        elif g*h==1:
            e=e+"S"
            for k in range(b):
                if c[k][j]=="P":
                    c[k]=0
                    l=l+1
        for k in range(l):
            c.remove(0)
        b=b-l
        if b==0:
            break
    print("Case #{}: {}".format(i+1,e))