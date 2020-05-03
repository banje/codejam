a=int(input())
for i in range(a):
    b=int(input())
    c=input()
    d=len(c)
    e=""
    for j in range(d):
        if c[j]=="E":
            e=e+"S"
        else:
            e=e+"E"
    print("Case #{0}: {1}".format(i+1,e))