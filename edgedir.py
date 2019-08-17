for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[None]*m
    b=[None]*m
    ans=0
    sheyy=[None]*m
    c=0
    if(n%2!=0):
        print(-1)
    else:
        for i in range(m):
            a[i],b[i]=map(int,input().split())
        for i in range(m):
            for j in range(m):
                if(a[i]==a[j])or(a[i]==b[j]):
                    c+=1
            if(c%2==0):
                ans+=1
            c=0
            for k in range(i+1,m):
                gadwal=0
                if(a[i]==a[k]):
                    sheyy[i]=0
                    sheyy[k]=0
                    gadwal=1
                    break
            if(gadwal==0)and(sheyy[i]==None):
                sheyy[i]=1
        if(ans!=m):
            print(-1)
        else: 
            print(" ".join(map(str,sheyy)))
