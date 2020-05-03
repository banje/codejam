import sys
a=list(map(int,input().split()))
for i in range(a[0]):
    c=0
    for j in range(-5,6):
        if c==1:
            break
        for k in range(-5,6):
            print(j,k)
            sys.stdout.flush()
            b=input()
            if b=="CENTER":
                c=1
                break