n=int(input())
aws=list(map(int,input().split()))
a=[]
b=[]
ans=0
for i in range(n-1):
    a1,b1=int(input().split())
    a.append(a1)
    b.append(b1)
    if(a[i]==1):
        lev=b[i]
w=set(aws[1:lev])
if(len(w)==lev-1):
    ans+=3
else:
    ans1=(lev-1)-len(w)-1
    ans+=lev-1-ans1
for i in range(n-1):
    
    
    
    
