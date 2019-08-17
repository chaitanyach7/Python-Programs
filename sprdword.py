t=int(input())
ans=[None]*t

for i in range(0,t):
    count=1
    n=int(input())
    a=list(map(int,input().split()))
    b=a
    
    n1=n
    fas=0
    if(b[fas]>=n):
        ans[i]=count
    else:
        for j in range(0,b[fas]+1):
            b[fas]+=b[j]
        count+=1
        while(True):
            n1=n-b[fas]+1
            if(b[fas]>=n1):
                ans[i]=count
                break
            else:
                
                count+=1
                for j in range(b[fas]-1,n=b[fas]):
                    b[fas]+=b[j]
for i in range(0,t):
    print(ans[i])
