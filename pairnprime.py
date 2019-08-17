for _ in range(int(input())):
    n,m=map(int,input().split())
    h=list(map(int,input().split()))
    c=list(map(int,input().split()))
    v=[h[0]]
    cv=[c[0]]
    for i in range(1,n):
        j=0
        while j < len(v):
            if v[j]<=h[i]:
                break
            j+=1
        print(v,cv)
        v=v[:j]+[h[i]]
        cv=cv[:j]+[c[i]]
        print(v,cv)
    print(len(set(cv)))
