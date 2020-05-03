a=list(map(int,input().split()))
for i in range(a[0]):
    if a[1]==10:
        b=[-1]*10
        for j in range(10):
            print(j+1)
            b[j]=int(input())
        for j in b:
            print(j,end="")
        print("")
    elif a[1]==20:
        b=[-1]*20
        for j in range(10):
            print(j+1)
            b[j]=int(input())
        c=[-1]*5
        c1=[-1]*5
        for j in range(5):
            print(j+1)
            c[j]=int(input())
            if c[j]==0:
                c1[j]=1
            else:
                c1[j]=0
        if (b[0:5]==c) or (b[0:5]==c1):
            d=[-1]*5
            for j in range(5):
                print(j+11)
                d[j]=int(input())
        else:
            