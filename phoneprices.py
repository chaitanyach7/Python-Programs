for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    c=1
    ans.append(a[0])
    for i in range(1,n):
        if(len(ans)>5):
            ans.pop(0)
        if(a[i]<min(ans)):
            c+=1
        ans.append(a[i])
    print(c)
