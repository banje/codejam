a=int(input())
for z in range(a):
    b=int(input())
    d=["",""]
    e=""
    for y in range(b):
        c=input()
        if e!="*":
            while "**" in c:
                c=c.replace("**","*")
            c=c.split("*")
            if len(c[0])>=len(d[0]):
                if c[0][:len(d[0])]==d[0] or d[0]=="":
                    d[0]=c[0]
                else:
                    e="*"
            else:
                if d[0][:len(c[0])]==c[0] or c[0]=="":
                    pass
                else:
                    e="*"
            if len(c[-1])>=len(d[-1]):
                if c[-1][-len(d[-1]):]==d[-1] or d[-1]=="":
                    d[-1]=c[-1]
                else:
                    e="*"
            else:
                if d[-1][-len(c[-1]):]==c[-1] or c[-1]=="":
                    pass
                else:
                    e="*"
            if len(c)>2:
                for y in range(len(c)-2,0,-1):
                    d.insert(1,c[y])
    if e!="*":
        for y in range(len(d)):
            e=e+d[y]
    print("Case #{}: {}".format(z+1,e))