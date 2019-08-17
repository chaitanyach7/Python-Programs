def validate(n,arr):
    a=0
    count=0
    if (arr[a]>=n):
        count=1
        return
    else:
        count+=1
        while(a<n):
            a+=arr[a]
            if(a>=n):
                count+=1
                break
    print(count)
            
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    validate(n,arr)
