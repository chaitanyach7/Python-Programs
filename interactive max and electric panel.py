import sys
import math
def func():
    a=[]
    cns=1000
    rt=int(math.sqrt(n))
    v=int(math.ceil(n/rt))
    google=v
    a.append(google)
    for i in range(n):
        if(a[i]<n):
            google+=v
            a.append(google)
        else:
            a.pop()
            a.append(n)
            break
    a.insert(0,1)
    l=len(a)
    for i in range(l):
        print(1,a[i])
        sys.stdout.flush()
        x=int(input())
        if(x==1 and a[i]==1):
            print(2)
            sys.stdout.flush()
            ans=1
            cns=0
            break
        elif(x==1 and a[i]!=1):
            print(2)
            sys.stdout.flush()
            ans=a[i-1]
            cns-=c
            break
    while(cns>0):
        print(1,ans)
        sys.stdout.flush()
        x=int(input())
        if(x==0):
            ans+=1
            cns-=1
        elif(x==1):
            break
    print(3,ans)
    sys.stdout.flush()
n,c=map(int,input().split())
sys.stdout.flush()
func()
'''rt=int(math.sqrt(n))
c=int(math.ceil(n/rt))
a=[1]
a.append(c)
for i in range(n):
    if(n>a[i]):
        a.append(a[i]+c)
    else:
        a.pop()
        a.append(n)
        break
l=len(a)
for i in range(l):
    print(1,a[i])
    sys.stdout.flush()
    x=int(input())
    if(x==1 and a[i]==1):
        print(2)
        sys.stdout.flush()
        ans=1
    if(x==1 and a[i] is not 1):
        print(2)
        sys.stdout.flush()
        ans=a[i-1]
        break
while(True):
    print(1,ans)
    sys.stdout.flush()
    x=int(input())
    if(x==0):
        ans+=1
    elif(x==1):
        break
print(3,ans)
sys.stdout.flush()'''
