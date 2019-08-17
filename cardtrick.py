for i in range(int(input())):
    z=0
    y=0
    k=0
    x=0
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*n
    o=a[0]
    for j in range(1,n):
        if(o>a[j]):
            z=1
            break
        o=a[j]
    if(z==1):
        x=j
        for j in range(x,n):
            b[k]=a[j]
            k+=1
        for j in range(0,x):
            b[k]=a[j]
            k+=1
        for j in range(1,n-1):
            if(b[j]>b[j+1]):
                y=1
    if(y==1):
        print('NO')
    else:
        print('YES')
    
    
