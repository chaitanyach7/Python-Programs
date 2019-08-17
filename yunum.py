for _ in range(int(input())):
    n=list(input().strip())
    ans=""
    mod=pow(10,9)+7
    for i in range(len(n)):
        n.insert(0,n.pop())
        ans="".join(map(str,n))+ans
    ans=int(ans)%mod
    print(ans)
