for _ in range(int(input())):
    d=int(input())
    a=[]
    b=[]
    for i in range(d):
        a1,a2=map(int,input().split())
        a.append(a1)
        b.append(a2)
    q=int(input())
    for i in range(q):
        sum1=0
        m,n=map(int,input().split())
        for i in range(d):
            if(a[i]<=m):
                sum1+=b[i]
        if(sum1>=n):
            print("Go Camp")
        else:
            print("Go Sleep")
