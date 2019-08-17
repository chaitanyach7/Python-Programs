import math
n,q=input().split()
n=int(n)
q=int(q)
x=[None]*n
y=[None]*n
r=[None]*n
for i in range(n):
    
    x[i],y[i],r[i]=input().split()
    x[i]=int(x[i])
    y[i]=int(y[i])
    r[i]=int(r[i])
for i in range(q):
    k=int(input())
    count1=0
    for j in range(360):
        x1=x[0]+r[0]*math.cos(math.radians(j))
        y1=y[0]+r[0]*math.sin(math.radians(j))
        x2=x[1]+r[1]*math.cos(math.radians(j))
        y2=x[1]+r[1]*math.sin(math.radians(j))
        if((x2-x1)*2+(y2-y1)*2==k):
            count1+=1
    print(count1)
