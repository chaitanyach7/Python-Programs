for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mx=0
    a.reverse()
    #print(a)
    b=[1 for x in range(n)]
    for i in range(n):
        if(a[i]%2==0):
            b[i]=0
    '''for i in range(n):
        c=0
        for j in range(i+1,n):
            if(a[j]%a[i]==0):
                c+=1
            if(mx-c)>=(n-j):
                break
        if(n-i<=mx):
            break
        if(mx<c):
            mx=c'''
    #print(b)
    for i in range(n):
        c=0
        if(b[i]==0):
            for j in range(i+1,n):
                if(b[j]==0):
                    if(a[j]%a[i]==0):
                        c+=1
                    if(mx-c)>=(n-j):
                        break
        else:
            if(a[i]==1):
                c=n-i-1
            else:
                for j in range(i+1,n):
                    if(a[j]%a[i]==0):
                        c+=1
                    if(mx-c)>=(n-j):
                        break
        #print(c)
        if(n-i<=mx):
            break
        if(mx<c):
            mx=c
    print(mx)
