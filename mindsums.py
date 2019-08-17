def digitsum(n):
    return int(sum(map(int,str(n))))
digsums=[]
ds=[]
for i in range(int(input())):
    n,d=input().split()
    n=int(n)
    d=int(d)
    n1=n
    k=1
    digsums.append(n1)
    ds.append(digitsum(n1))
    n1+=d
    for j in range(1,1000):
        digsums.append(digitsum(n1))
        ds.append(digitsum(digsums[k]))
        n1=digsums[k]+d
        k+=1
    minv=digsums[0]
    minu=ds[0]
    ind=0
    jnd=0
    for j in range(len(digsums)):
        if(minv>digsums[j]):
            minv=digsums[j]
            ind=j
        if(minu>ds[j]):
            minu=ds[j]
            jnd=j
    print(min(minv,minu),min(ind+1,jnd*2))
    digsums=[]
    ds=[]
