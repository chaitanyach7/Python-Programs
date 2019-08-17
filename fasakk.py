from collections import deque
n,q,k=map(int,input().split())
a=list(map(int,input().split()))
s=input().strip()
s=list(s)
b=[]
for i in range(n):
    c=0
    mc=0
    for j in a:
        if(j==1):
            c+=1
        else:
            c=0
        if(mc<c):
            mc=c
    b.append(min(mc,k))
    a=deque(a)
    a.rotate()
    a=list(a)
w=0
for i in range(q):
    #print(s)
    if(s[i]=='!'):
        w+=1
    elif(s[i]=='?'):
        if(w==n-1):
            w=0
        print(b[w])
