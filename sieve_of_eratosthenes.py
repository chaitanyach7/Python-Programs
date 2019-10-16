n=int(input())
p=2
arr=[1 for i in range(n+1)]
while(p*p<=n):
    for i in range(p*p,n+1,p):
        if(arr[i]):
            arr[i]=0
    p+=1
for i in range(2,n+1):
    if(arr[i]):
        print(i,end=" ")
