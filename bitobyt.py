t=int(input())
ans=[[0,0,0]]*t
for i in range(t):
    n=int(input())
    n=n-1
    bits=0
    rem=n/26
    bits=int(2**rem)
    if(n%26<2):
        ans[i][0]=bits
    else:
        ans[i][0]=0
    if(n%26>=2)and(n%26<10):
        ans[i][1]=bits
    else:
        ans[i][1]=0
    if(n%26>=10)and(n%26<26):
        ans[i][2]=bits
    else:
        ans[i][2]=0
    print(ans[i][0],ans[i][1],ans[i][2])
    
    
    
