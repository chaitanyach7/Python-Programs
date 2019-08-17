from math import gcd
from itertools import product
for _ in range(int(input())):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    c=a.count(-1)
    ans=0
    sum1=0
    cm=[]
    w=[]
    for i in range(n):
        if(a[i]==-1):
            b.append(i)
        else:
            sum1+=a[i]
    #print(sum1)
    w.append(1)
    if(c>=1):
        for x in range(2,s-sum1):
            w.append(x)
        #print(w)
        cm=list(product(w,repeat=c))
        for i in range(len(cm)):
            #for j in range(c):
                #s2+=cm[i][j]
            #if(s2==s):
            for j in range(c):  
                a[b[j]]=cm[i][j]
            if(sum(a)==s):
                #print(a)
                for j in range(n-1):
                    for k in range(j+1,n):
                        ans+=gcd(a[j],a[k])
    else:
        for j in range(n-1):
            for k in range(j+1,n):
                ans+=gcd(a[j],a[k])
    print(ans)
        
