for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=[]
    b=[pow(k,a[0])]
    d=[b[0]]
    mn =0
    mni=0
    for i in range(1,n):
        b.append(pow(k,a[i]))
        d.append(d[i-1]+b[i])
    for i in range(1,n):
        c.append(d[i-1]*(d[n-1]-d[i-1]))
        if(mn<c[i-1]):
            mn=c[i-1]
            mni=i-1
    print(mni+1)
