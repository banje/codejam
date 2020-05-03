a=int(input())
for z in range(a):
    b=input().split()
    c=[int(b[0]),int(b[1])]
    for y in range(c[0]):
        if y<len(b[2]):
            if b[2][y]=="N":
                c[1]=c[1]+1
            else:
                c[1]=c[1]-1
    d=c[0]
    if c[1]==0:
        print("Case #{}: {}".format(z+1,d))
    else:
        for y in range(c[0],len(b[2])):
            if b[2][y]=="N":
                c[1]=c[1]+1
            else:
                c[1]=c[1]-1
            if c[1]>0:
                c[1]=c[1]-1
            if c[1]<0:
                c[1]=c[1]+1
            d=d+1
            if c[1]==0:
                print("Case #{}: {}".format(z+1,d))
                break
        else:
            print("Case #{}: IMPOSSIBLE".format(z+1))