for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    sum1=[0]*n
    f=0
    for i in range(n):
        w=0
        for j in range(i+1,0,-1):
            sum1[w]+=(a[i]//j)
            #print(sum1[w],a[i],j)
            #print(a[i]//j,a[i],j)
            #print(j-1,sum1[j-1])
            w+=1
    #print(sum1)
    for i in range(n):
        if(sum1[i]<=k):
            print(i+1)
            f=1
            break
    if(f==0):
        print(n+1)
