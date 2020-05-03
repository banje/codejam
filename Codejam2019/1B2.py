a=input().split()
b=int(a[1])
a=int(a[0])
import numpy as np
for i in range(a):
    if b==6:
        print("1")
        c=int(input())
        print("2")
        d=int(input())
        print("3")
        e=int(input())
        print("4")
        f=int(input())
        print("5")
        g=int(input())
        print("6")
        h=int(input())
        j=np.array([c, d, e, f, g, h])
        k=np.array([[2, 1, 1, 1, 1, 1],
                    [4, 2, 1, 1, 1, 1],
                    [8, 2, 2, 1, 1, 1],
                    [16, 4, 2, 2, 1, 1],
                    [32, 4, 2, 2, 2, 1],
                    [64, 8, 4, 2, 2, 2]])
        l=np.linalg.inv(k).dot(j)
        print("{} {} {} {} {} {}".format(int(round(l[0])),int(round(l[1])),int(round(l[2])),int(round(l[3])),int(round(l[4])),int(round(l[5]))))
        m=int(input())
    else:
        print("1")
        c=int(input())
        print("2")
        d=int(input())
        print("1 1 1 1 1 1")
        m=int(input())
    if m==-1:
        break