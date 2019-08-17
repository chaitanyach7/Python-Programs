for i in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    a=[[]*m]*n
    n1=n+m-2
    m1=[]
    for j in range(n):
        a[j]=input()
        a[j]=list(a[j])
    for k in range(0,n):
        for b in range(0,m):
            if(a[k][b]=='1'):
                for k1 in range(0,n):
                    for b1 in range(0,m):                        
                        if(a[k1][b1]=='1'):
                            #print(k1,b1)
                            m1.append(abs(k-k1)+abs(b-b1))
    #print(m1)
    for j in range(1,n1+1):
        print(int(m1.count(j)/2))
                                    
