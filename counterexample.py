import collections as cl

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=cl.Counter(a)
    a=c.most_common(len(c))
    ans=[]
    print(a)
