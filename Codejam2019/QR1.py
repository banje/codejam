a=int(input())
for i in range(a):
    c=input()
    b=int(c)
    d=len(c)
    e=0
    for j in range(d):
        if int(c[j])==4:
            b=b-10**(d-j-1)
            e=e+10**(d-j-1)
    print("Case #{2}: {0} {1}".format(b,e,i+1))