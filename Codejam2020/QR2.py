a=int(input())
for i in range(a):
    b=input()
    c=0
    d=""
    for j in range(len(b)):
        if c<int(b[j]):
            d=d+"("*(int(b[j])-c)
            c=int(b[j])
        elif c>int(b[j]):
            d=d+")"*(c-int(b[j]))
            c=int(b[j])
        d=d+b[j]
    d=d+")"*c
    print("Case #{}: {}".format(i+1,d))