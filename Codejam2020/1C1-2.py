a=int(input())
for z in range(a):
    b=input().split()
    c=[int(b[0]),int(b[1])]
    for y in range(len(b[2])):
        if b[2][y]=="N":
            c[1]=c[1]+1
        elif b[2][y]=="S":
            c[1]=c[1]-1
        elif b[2][y]=="E":
            c[0]=c[0]+1
        else:
            c[0]=c[0]-1
        if abs(c[0])+abs(c[1])<=y+1:
            print("Case #{}: {}".format(z+1,y+1))
            break
    else:
        print("Case #{}: IMPOSSIBLE".format(z+1))