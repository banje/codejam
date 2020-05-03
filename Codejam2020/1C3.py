a=int(input())
for z in range(a):
    [b,c]=list(map(int,input().split()))
    d=list(map(int,input().split()))
    d.sort()
    f=0
    for y in d:
        e=d.count(y)
        if f<e:
            f=e
            g=y
    if f>=3:
        print("Case #{}: {}".format(z+1,0))
    elif f==2:
        if c==3:
            for y in d:
                if y>g:
                    print("Case #{}: {}".format(z+1,1))
                    break
            else:
                if (g/2 in d) or (g*2 in d):
                    print("Case #{}: {}".format(z+1,1))
                else:
                    print("Case #{}: {}".format(z+1,2))
        else:
            print("Case #{}: {}".format(z+1,0))
    else:
        if c==3:
            if (g/2 in d) or (g*2 in d):
                print("Case #{}: {}".format(z+1,1))
            else:
                print("Case #{}: {}".format(z+1,2))
        else:
            print("Case #{}: {}".format(z+1,1))