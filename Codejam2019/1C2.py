a=input().split()
b=int(a[1])
a=int(a[0])
from itertools import permutations as pm
c=["A","B","C","D","E"]
d=[]
e=""
for i in pm(c,5):
    for j in range(5):
        e=e+i[j]
    d.append(e)
    e=""
for i in range(a):
    h=d
    for j in range(118):
        g=""
        for k in range(4):
            e=j*5+k+1
            print(e)
            f=input()
            g=g+f
        if "A" not in g:
            g=g+"A"
        elif "B" not in g:
            g=g+"B"
        elif "C" not in g:
            g=g+"C"
        elif "D" not in g:
            g=g+"D"
        else:
            g=g+"E"
        h.remove(g)
    l=h[0]
    m=h[1]
    j=0
    while j<5:
        if l[j]!=m[j]:
            print(591+j)
            n=input()
            if n==l[j]:
                print(m)
                o = input()
                break
            else:
                print(l)
                o = input()
                break
        j=j+1