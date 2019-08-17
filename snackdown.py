def func(n,a,b):
    k=1
    for j in range(0,n-2):
        if(a[j]<b[j]):
            k=b[j]-a[j]
            a[j]+=k
            a[j+1]+=k*2
            a[j+2]+=k*3
    c=0
    for j in range(0,n):
        if(a[j]==b[j]):
            c+=1

    if(c==n):
        print('TAK')
    else:
        print('NIE')

t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    func(n,a,b)
