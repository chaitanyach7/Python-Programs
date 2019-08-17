#from itertools import combinations
def fassk(ans):
    mod=pow(10,9)+7
    m1=a[0]
    m2=b[0]
    for i in range(1,len(a)):
        if(m1<a[i]):
            m1=a[i]
        if(m2<b[i]):
            m2=b[i]
    for i in range(len(a)):
        ans=(ans+(m1*b[i])%mod)%mod
    ans=(ans+(m1*m2)%mod)%mod
    '''for i in range(len(b)):
        ans=(ans+(m2*a[i])%mod)%mod
    ans=(ans+(m1*m2)%mod)%mod'''
    #print(ans)
    a.remove(m1)
    b.remove(m2)
    if(len(a)==0)or(len(a)==1):
        print(ans)
        return 0
    else:
        fassk(ans)
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    fassk(ans)
    
